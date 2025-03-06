const { create } = require('venom-bot');
const fs = require('fs').promises; // Usa versão assíncrona
const filePath = 'functions/info.json';
const messagePath = 'functions/message.json';
let isProcessing = false

async function saveMessages(data) {
    try {
        let currentData = {};

        try {
            const jsonData = await fs.readFile(filePath, 'utf8');
            currentData = JSON.parse(jsonData);
        } catch (error) {
            if (error.code !== 'ENOENT') {
                console.error('Erro ao ler JSON:', error);
                return;
            }
        }

        if (!currentData.users) {
            currentData.users = {};
        }

        const userId = data.user;
        if (!currentData.users[userId]) {
            currentData.users[userId] = [];
        }

        currentData.users[userId].push(data.message);

        await fs.writeFile(filePath, JSON.stringify(currentData, null, 2), 'utf8');
        console.log('Mensagem salva com sucesso!');
    } catch (error) {
        console.error('Erro ao salvar a mensagem:', error);
    }
}

async function sendMessage(client, message, id) {
    try {
        await client.sendText(id, message);
        console.log(`Mensagem enviada para ${id}: ${message}`);
    } catch (error) {
        console.error('Erro ao enviar a mensagem:', error);
    }
}

async function checkMessage(client) {
    if (isProcessing) {
        console.log("Já está processando mensagens, aguardando o término...");
        return;
    }

    try {
        isProcessing = true;

        try {
            jsonData = await fs.readFile(messagePath, 'utf8');
            currentData = JSON.parse(jsonData);
        } catch{
            currentData = {}
        }

        if (!currentData.messages || currentData.messages.length === 0) {
            console.log("Nenhuma mensagem para enviar.");
            return;
        }

        console.log("Enviando mensagens...");
        for (let messageData of currentData.messages) {
            const message = messageData.message;
            const id = messageData.id;
            await sendMessage(client, message, id); 
        }

        console.log("Todas as mensagens foram enviadas, agora limpando a lista...");
        await fs.writeFile(messagePath, JSON.stringify({ "messages": [] }, null, 2), 'utf8');
        console.log("Lista de mensagens limpa com sucesso.");

    } catch (error) {
        console.error("Erro ao processar as mensagens:", error);
    } finally {
        isProcessing = false;
    }
}

create({
    session: 'my-session',
    browserPathExecutable: '/snap/bin/chromium',
    browserArgs: ['--headless=new', '--no-sandbox', '--disable-gpu']
})
.then((client) => {
    start(client);
    setInterval(async () => {
        await checkMessage(client);  
    }, 5000);
})
.catch((error) => console.log(error));

function start(client) {
    console.log('Bot Iniciado com sucesso.')
    client.onMessage((message) => {
        if (message.body) {
            console.log(`Mensagem recebida de ${message.sender.id}: ${message.body}`);

            const messageContent = {
                user: message.from,
                message: message.body 
            };
            saveMessages(messageContent);
        }
    });
}