# CORTEX

A fork of [DAVE](https://github.com/gabrielchua/dave).

## Acknowledgments

This project is a fork of the original [DAVE](https://github.com/gabrielchua/dave) by [Gabriel Chua](https://gabrielchua.me/).

## Quick Start

1. Clone this repository
2. Install the required dependencies by running

```python
pip install -r requirements.txt
```
   
3. Modify `create_assistant.py` as needed, and note down the `ASSISTANT_ID`.
4. Create a `secrets.toml` file located within the `.streamlit/` directory. It should minimally contain these variables: `OPENAI_API_KEY`, `ASSISTANT_ID`
5. Launch the application:

```python
streamlit run demo_app.py
```
