from fastapi import FastAPI

app = FastAPI(
    title="Formatting App")


@app.get("/formatted-text")
def space_formatting(text: str = "Hello world."):
    temp_text = list(text)
    for i in range(len(temp_text) - 1):
        if temp_text[i] == temp_text[i + 1]:
            if temp_text[i] == ' ':
                temp_text[i] = ''
        if temp_text[i] == ' ' and temp_text[i+1] == ',' or (temp_text[i] == ' ' and temp_text[i+1] == '.'):
            if temp_text[i] == ' ':
                temp_text[i] = ''
    text3 = ''.join(map(str, temp_text))
    return text3


