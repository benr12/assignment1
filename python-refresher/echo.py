#echo.py

def echo(text: str, repetitions: int = 3) -> str:
   echoList = [text[-i:] for i in range(repetitions, 0, -1)]
   return "\n".join(echoList) + "\n."
       

if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))