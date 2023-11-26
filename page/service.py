import g4f

class GPTService:
    @staticmethod
    def generate_recipe(prompt):
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            stream=True,
        )

        sentence = ''

        for message in response:
            sentence = str(sentence + message)

        return sentence