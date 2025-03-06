from models.ai_model import generate_and_send_responses
import asyncio

async def run_node_process():
    process = await asyncio.create_subprocess_exec(
        "node", "functions/bot.js",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    try:
        while True:
            output = await process.stdout.readline()
            if output:
                print(output.decode().strip())
            generate_and_send_responses()
    except asyncio.CancelledError:
        print("Encerrando o servidor...")
        process.terminate()
        await process.wait()

async def main():
    try:
        await run_node_process()
    except KeyboardInterrupt:
        print("Processo interrompido manualmente.")

if __name__ == "__main__":
    asyncio.run(main())
