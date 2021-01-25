# Load the pandas libraries with alias of 'pd'
import pandas as pd
import matplotlib.pyplot as plt

# Setting pandas options
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

def main():
    # Read .csv file
    dataset = pd.read_csv(r'C:\Users\alexd\Documents\VScode Projects\Python Projects\FinanceMonitor\test.csv')

    # Format dataset
    dataset.dropna(subset = ["Debit"], inplace=True)
    #del dataset['Credit']
    #del dataset['Balance']

    # Print statistics of dataset
    print('Number of columns in csv file: ', len(dataset.columns))
    print('Number of transactions in csv file: ', len(dataset.index))

    # Print .csv file
    #print(dataset)

    # Preparing the data for CompA
    DateX =  dataset['Date'].tolist() 
    BalanceY = dataset['Balance'].tolist()
    DebitY = dataset['Debit'].tolist()

    # Plot Balance over Time
    plt.plot(DateX, BalanceY, linewidth=3, label='Balance Over Time')
    # Display Title
    plt.title('Visualisation of Balance Over Time')
    # Set YLabel
    plt.ylabel('Dollars ($)')
    # Set XLabel
    plt.xlabel('Date')
    # Add legend
    plt.legend()
    # Display Grid
    plt.grid(True)
    # Save the plot as a .png
    plt.savefig(r'C:\Users\alexd\Documents\VScode Projects\Python Projects\FinanceMonitor\plotPNGs\BalanceOverTime.png')
    # Show the plot
    plt.show()

    # Plot Balance over Time
    plt.plot(DateX, DebitY, linewidth=3, label='Balance Over Time')
    # Display Title
    plt.title('Visualisation of Debit Over Time')
    # Set YLabel
    plt.ylabel('Dollars ($)')
    # Set XLabel
    plt.xlabel('Date')
    # Add legend
    plt.legend()
    # Display Grid
    plt.grid(True)
    # Save the plot as a .png
    plt.savefig(r'C:\Users\alexd\Documents\VScode Projects\Python Projects\FinanceMonitor\plotPNGs\DebitOverTime.png')
    # Show the plot
    plt.show()

main()

