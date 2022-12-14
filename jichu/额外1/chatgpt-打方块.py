import openai,os
start_sequence = "\nA:"
restart_sequence = "Q: "
# Replace `<your_api_key>` with your actual OpenAI API key
openai.api_key = "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"
prompt = " "
while len(prompt)!=0:
    # Ask a question
    prompt = input(restart_sequence)
    #prompt = "tell me in Chinese:" + input("\n请输入要翻译的内容：")

    # Get my answer
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=2000,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Print my answer
    print(start_sequence,response["choices"][0]["text"].strip())
