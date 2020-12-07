# Stock Prediction 
Final assignmetn in DAT 540 Introduction to Data Science

Groupname: Nordre Hafrsfjord Karsk og TENNIS	
Lars B. Lukerstuen (248800)
Joakim O. Gjermundstad (251365)
Martin Sommerli (258753)


## Installation 
To run this project you must be able to run .ipynb files. 
We recommend using Anaconda as Juptyer Notebook is pre-packaged with all necessary components to run our project

From the Anaconda promp, run the following command
```python
jupyter notebook
```
You will now be able to open the notebook in your desired browser.

## Features

In the Results-tab of the notebook you may set your desired ticker, and the model will guess the next closing price of the stock.
The results from the ANN will also be displayed 

```python
import main

main.run(ticker = 'Your desired ticker', start_date = 'YYYY-MM-DD')
```
 