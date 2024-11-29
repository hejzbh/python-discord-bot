from openai import OpenAI

class Summarizer:
    def __init__(self, api_key):
        self.api_key = api_key
        print(api_key)
        self.client = OpenAI(api_key=api_key)
        
    def summarize(self, content):
        try:
            # Try to summarize content
            completion = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "Summarize this text in 2-3 sentences."},
                    {"role": "user", "content": content}
                ]
            )

            # Return summary if its done
            return completion.choices[0].message

        except Exception as e:   
            # error
            print(f"An error occurred: {e}")
            return content