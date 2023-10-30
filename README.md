# SAT Q&A: Question Answering System based on Google Palm LLM and langchain for SAT questions on world_history and us_history  

This is an end to end LLM project based on Google Palm and Langchain. I have built a Q&A system for students preparing for SAT examination. SAT is a standardized test widely used for college admissions in the United States. This system will provide a streamlit based user interface for students where they can ask questions and get answers. Currently the application is focused on questions related to **us_history** and **world_history**

## Project Architecture

![SAT_QA arch](https://github.com/MaruthiKo/SAT_QA/assets/63769209/e05daf59-e57a-492e-b2a7-e078dae4fc04)

## Interface Demo


https://github.com/MaruthiKo/SAT_QA/assets/63769209/054d2974-ae80-4052-b667-9f8595a05ad1




## Project Highlights
- Use a real CSV file of SAT Question and Answers on us_history and world_history.
- Student who are attempting the SAT exam refer previous year paper for practice.
- I built an LLM based question and answer system that can reduce the workload of searching answers.
- Students should be able to use this system to ask questions directly and get answers within seconds.

## Technologies Used:
- Langchain + Google Palm: LLM based Q&A
- Streamlit: UI
- Huggingface instructor embeddings: Text embeddings
- FAISS: Vector database

## Installation
1. Clone this repository to your local machine using:

```bash
  git clone https://github.com/MaruthiKo/SAT_QA.git
```
2. Navigate to the project directory:
   
```bash
  cd SAT_QA
```
3. Install the required dependencies using pip:
   
```bash
  pip install -r requirements.txt
```
4. Acquire an api key through makersuite.google.com and put it in .env file
```bash
  GOOGLE_API_KEY="your_api_key_here"
```
## Usage

1. Run the Streamlit app by executing:

```bash
streamlit run main.py
```
2. The web app will open in your browser.
   - To create knowledge base uncomment the line in langchain_helper, create vector_db. It will take some time before knowledgebase is created so please wait.
   - Once knowledge base is created you will see a directory called `faiss_index` in your current folder. 
   - Now you are ready to ask questions. Type your question in Question box and hit Enter

## Sample Questions
 - The Kush city of Meroe rose to prominence mainly because of its natural supply of
 - Usage of the Silk Roads for trade declined near the end of the Han dynasty primarily due to
 - The Seven Years' War was MOST beneficial for which nation?
 - The Louisiana Purchase provided France with significant funding for
 - President Johnson called for a voting rights bill in 1965 after

## Project Structure
- main.py: The main Streamlit application script.
- langchain_helper.py: This has all the langchain code
- requirements.txt: A list of required Python packages for the project.
- .env: Configuration file for storing your Google API key.
