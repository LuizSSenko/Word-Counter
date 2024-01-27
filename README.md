# Word-Counter
Used to identify the most common words in job postings and create a more AI-aligned CV based on them.

Tired of sending out hundreds of resumes and not landing a job?
This software will assist you in crafting a better resume by pinpointing the keywords hiring managers use to screen candidates.

Note: Feel free to edit the script and select a different job platform, but make sure that all the links used in the urls.txt file are from the same platform (due to the HTML data structure).

## Basic workflow
- Download the software.
- Create a file named urls.txt within the software folder.
- Visit Agrobase.com.br, find the job listings you're interested in, copy the link, and paste it into the urls.txt file.
- Run the software.
- Analyze the graph.

# How to Use
## Visit the website and find some interesting job openings

![image](https://github.com/LuizSSenko/Word-Counter/assets/140913035/2d42b1a8-061d-42a2-8175-20d17838834f)


## Copy the links of the pages and paste them into the urls.txt file, one link per line

![image](https://github.com/LuizSSenko/Agrobase.com.br-Word_Counter/assets/140913035/e1dd3b90-7f64-4839-aa3b-4d103292cd4f)

## Run the script
- To get started, you'll need to specify the HTML tags that mark the beginning and end of the website section you want to search within, so that irrelevant data can be excluded.
- To find this information, right-click on a page and select "inspect." In the example below, it starts with "u1" and ends with "/u1." This pattern is likely consistent across all pages within the same platform, but it's a good practice to verify occasionally.

![image](https://github.com/LuizSSenko/Word-Counter/assets/140913035/6adb32b2-5b15-4184-ba1b-c00b69ee747d)

- A popup will ask you the start and end tag of the section with the good information are located, write the ones you found.
  
![image](https://github.com/LuizSSenko/Word-Counter/assets/140913035/829eec01-fe37-418a-801b-c8650e18842e)

- A popup will prompt you to provide the start and end tags of the section containing the relevant information. Enter the tags you've identified.

![image](https://github.com/LuizSSenko/Word-Counter/assets/140913035/02a20f4a-3514-4fb8-a013-29c6b1420dae)

- An interactive graph will be generated (the example shown includes more than 20 of the most frequently used words).

![Figure_1](https://github.com/LuizSSenko/Agrobase.com.br-Word_Counter/assets/140913035/89e5eda5-cca8-4dc3-9ec9-7694583fe203)

## Analyzing the Results
When examining the results, you should consider which of these words could be "keywords" in candidate filtering. In this case, I believe they might include:
- Produtos
- Vendas
- Clientes
- Relatórios
- Comercial
- Desenvolvimento
- Negociação.....

### Now, you can edit your resume while incorporating these keywords into it (but remember, no exaggerations or falsehoods!).
