<p align="center">
  <a href="https://user-images.githubusercontent.com/101568457/208002599-be7000ca-e05a-4706-99b2-49bc5a35e367.png"><img src="https://user-images.githubusercontent.com/101568457/208002599-be7000ca-e05a-4706-99b2-49bc5a35e367.png" alt="FastAPI"></a>
</p>
<p align="center">
    <em>Keep your ngrok free tier alive, forever</em>
</p>

---
<h1>
! Use this tool for personal use only, for prototyping projects and related things. For commercial or production use consider subscribing to ngrok.
</h1>

## Prerequisites
* Ngrok already configured with your key
* A bot on telegram
---
## installation

* With pip
    ```
    pip3 newgrok
    ```

* With poetry:

    ```
    poetry add newgrok
    ```
---
## Variables
|           |                                                 |
|-----------|-------------------------------------------------|
| app_port  | Port of the application running on your machine |
| protocol  | Network protocol you want to use                |
| bot_token | Your bot token in telegram                      |
| chat_id   | The id of the chat between the bot and you      |
---
## Setup

* First you need to set the environment variables, chat_id for later, edit the ```.env``` file
    ```
    app_port=8000
    protocol=http
    bot_token=******************************
    chat_id=
    ```
* To get the chat_id, run:
    ```
    chat_id
    ```
    Now send a message to the bot, and it will reply with the chat_id. Complete the ```.env``` file
    ```
    app_port=8000
    protocol=http
    bot_token=******************************
    chat_id=********
    ```
* Now with these 3 lines of code, newgrok is already running, enjoy
    ```python
    from newgrok import Newgrok

    ngrok = Newgrok()
    ngrok.run()
    ```
