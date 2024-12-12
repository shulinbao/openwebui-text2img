import aiohttp
from pydantic import BaseModel, Field


async def emit(emitter, msg, done):
    await emitter(
        {
            "type": "status",
            "data": {
                "done": done,
                "description": msg,
            },
        }
    )


class Filter:
    class Valves(BaseModel):
        priority: int = Field(
            default=0,
            description="Priority level for the filter operations.",
        )
        api_url: str = Field(
            default="https://your-one-api-address/v1",
            description="Base URL for the One API.",
        )
        api_key: str = Field(
            default="",
            description="API Key for the One API.",
        )

    class UserValves(BaseModel):
        size: str = Field(
            default="1024x1024",
            description="1024x1024, 512x512",
        )
        steps: int = Field(
            default=20,
            description="Number of inference steps to be performed. (1-100)",
        )
        model: str = Field(
            default="dall-e-3",
            description="The name of the model.",
        )

    def __init__(self):
        self.valves = self.Valves()

    async def inlet(self, body, __user__, __event_emitter__):
        await emit(__event_emitter__, "Generating prompt, please wait...", False)
        return body

    async def request(self, prompt, __user__):
        url = f"{self.valves.api_url}/images/generations"

        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": f"Bearer {self.valves.api_key}",
        }

        payload = {
            "prompt": prompt,
            "model": __user__["valves"].model,
            "image_size": __user__["valves"].size,
            "num_inference_steps": __user__["valves"].steps,
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload, headers=headers) as response:
                response.raise_for_status()
                ret = await response.json()
                return ret

    async def outlet(self, body, __user__, __event_emitter__):
        await emit(__event_emitter__, f"Generating pictures, please wait...", False)
        prompt = body["messages"][-1]["content"]
        res = await self.request(prompt, __user__)

        image_url = res["data"][0]["url"]
        mdout = f"![image]({image_url})"
        body["messages"][-1]["content"] += f"\n\n{mdout}"

        await emit(
            __event_emitter__, f"Generated successfully, click to preview!", True
        )

        return body
