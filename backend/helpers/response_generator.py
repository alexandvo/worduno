from openai import OpenAI
from math import floor

def getResponse(client: OpenAI, inputMessage: str):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {
                "role": "system",
                "content": "You will receive text and your job is to simplify each sentence individually by making the language less complex, easy to digest for the common man, and easier to comprehend. This is very important but you will NOT do this simplification and you will NOT remove things on important data points such as titles (article titles, video titles, document titles, book titles, etc.), numbers, and proper nouns (John, Steve, etc.). This means your response MUST includes the original titles, numbers, and proper nouns in the input text."
            },
            {
                "role": "user",
                "content": inputMessage
            }
        ],
        temperature=0,
        max_tokens=(floor(len(inputMessage)*1.5)),
        top_p=0
    )
    return response.choices[0].message.content

# message = "Achieving cost and performance efficiency for cloud-hosted databases requires exploring a large configuration space, including the parameters exposed by the database along with the variety of VM configurations available in the cloud. Even small deviations from an optimal configuration have significant consequences on performance and cost. Existing systems that automate cloud deployment configuration can select near-optimal instance types for homogeneous clusters of virtual machines and for stateless, recurrent data analytics workloads. We show that to find optimal performance-per-$ cloud deployments for NoSQL database applications, it is important to (1) consider heterogeneous cluster configurations, (2) jointly optimize database and VM configurations, and (3) dynamically adjust configuration as workload behavior changes. We present OPTIMUSCLOUD, an online reconfiguration system that can efficiently perform such joint and heterogeneous configuration for dynamic workloads. We evaluate our system with two clustered NoSQL systems: Cassandra and Redis, using three representative workloads and show that OPTIMUSCLOUD provides 40% higher throughput/$ and 4.5× lower 99-percentile latency on average compared to state-of-the-art prior systems, CherryPick, Selecta, and SOPHIA."

# print(getResponse(client, message))
