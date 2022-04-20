# no box around legend
plt.legend(frameon=False)

# de-spining to remove axises
sns.despine(left=True, bottom=True)

# Numerical labels on bar charts
#Here, 'labels' refers to the bigrams on the y-axis
#i.e. 'Look forward', 'Jó éjt', etc.
#and X is the list of values determining bar length
#Loop through these labels
for n, i in enumerate(labels):
    #Create an axis text object
    ax.text(X[n]-0.003, #X location of text (with adjustment)
            n, #Y location
            s=f'{round(X[n],3)}%', #Required label with formatting
            va='center', #Vertical alignment
            ha='right', #Horizontal alignment
            color='white', #Font colour and size
            fontsize=12)
