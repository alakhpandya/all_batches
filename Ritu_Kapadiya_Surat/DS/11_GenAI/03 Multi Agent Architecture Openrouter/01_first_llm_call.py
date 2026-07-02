from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    
    base_url= "https://openrouter.ai/api/v1",

    api_key= os.getenv("OPENROUTER_API_KEY")
)

response = client.chat.completions.create(

    model = "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",

    messages = [{

        "role" : "user",
        
        "content" : "What does Ricoh company do?"

    }]

)

# print(response)

# The response:
"""
ChatCompletion(id='gen-1782875569-uXyqao0CzGAfIQAixi7Z', 
    choices=[
        Choice(finish_reason='stop', index=0, logprobs=None, 
               message=ChatCompletionMessage(
                   content='Ricoh\u202fCo., Ltd. is a Japanese multinational corporation that provides a wide range of products and services centered around imaging, printing, and document management. Its core business activities include:\n\n| Business Area | What It Does |\n|---------------|--------------|\n| **Imaging & Printing Equipment** | Designs, manufactures, and sells office hardware such as laser printers, multifunction printers (MFPs), digital copiers, and production printing systems. |\n| **Document Solutions** | Offers managed print services, print‑on‑demand solutions, workflow automation, and document‑management software that help businesses streamline how they create, share, and store paper and digital documents. |\n| **IT & Software Services** | Provides IT infrastructure services, cloud‑based document solutions, cybersecurity tools, and custom software development (e.g., document‑management platforms, workflow automation, AI‑driven analytics). |\n| **Business Solutions & Consulting** | Supplies industry‑specific solutions (e.g., healthcare, finance, education, government) that integrate hardware, software, and services to improve productivity and compliance. |\n| **Digital Innovation** | Invests in emerging technologies such as AI‑based image recognition, IoT for device management, and sustainable printing technologies (e.g., energy‑efficient devices, recycled paper solutions). |\n\n**Key Points**\n\n- **Headquarters:** Tokyo, Japan.  \n- **Global Presence:** Operates in more than 150 countries with regional offices and a network of partners and service providers.  \n- **Historical Roots:** Founded in 1936 as the Riken Company; the name “Ricoh” comes from “direct copy” (from the Japanese phrase *ri‑kō*).  \n- **Revenue & Scale:** A Fortune‑500‑class company with annual revenues in the tens of billions of dollars, serving millions of customers worldwide.  \n\nIn short, Ricoh is best known for its office imaging hardware (printers, copiers, scanners) and the accompanying software and services that help organizations manage, automate, and secure their document workflows.', 
                   refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=None, 
                   reasoning='The user asks: "What does Ricoh company do?" They want a description of what Ricoh does. Provide concise answer: Ricoh is a Japanese multinational corporation specializing in office equipment (printers, copiers, imaging), digital solutions, IT services, imaging and electronics. Also mention its business segments: imaging and printing, document solutions, IT services, and its presence in various industries. Provide overview.\n', 
                   reasoning_details=[{'type': 'reasoning.text', 'text': 'The user asks: "What does Ricoh company do?" They want a description of what Ricoh does. Provide concise answer: Ricoh is a Japanese multinational corporation specializing in office equipment (printers, copiers, imaging), digital solutions, IT services, imaging and electronics. Also mention its business segments: imaging and printing, document solutions, IT services, and its presence in various industries. Provide overview.\n', 'format': 'unknown', 'index': 0}]
                ), 
            native_finish_reason='stop'
        )
    ], 
    created=1782875569, model='nvidia/nemotron-3-nano-omni-30b-a3b-reasoning-20260428:free', object='chat.completion', moderation=None, service_tier=None, system_fingerprint=None, 
    usage=CompletionUsage(completion_tokens=527, prompt_tokens=23, total_tokens=550, completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=None, audio_tokens=0, reasoning_tokens=108, rejected_prediction_tokens=None, image_tokens=0), prompt_tokens_details=PromptTokensDetails(audio_tokens=0, cached_tokens=0, cache_write_tokens=0, video_tokens=0), cost=0, is_byok=False, cost_details={'upstream_inference_cost': 0, 'upstream_inference_prompt_cost': 0, 'upstream_inference_completions_cost': 0}), 
    provider='Nvidia'
)
"""
print("Agent:", response.choices[0].message.content)