# import all modules
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Read in the DataFrame
df = pd.read_csv(grant_file)


# Display pandas histogram
df['Award_Amount'].plot.hist()
plt.show()

# Clear out the pandas histogram
plt.clf()


# Create a displot
sns.displot(df['Award_Amount'],
             bins=20)

# Display the plot
plt.show()


# Create a displot of the Award Amount
sns.displot(df['Award_Amount'],
             kind='kde',
             rug=True,
             fill=True)

# Plot the results
plt.show()


# Create a regression plot of premiums vs. insurance_losses
sns.regplot(data=df, x="insurance_losses"
, y="premiums" )



# Display the plot
plt.show()


# Create a regression plot using hue
sns.lmplot(data=df,
           x="insurance_losses",
           y="premiums",
           hue="Region")

# Show the results
plt.show()


# Create a regression plot with multiple rows
sns.lmplot(data=df,
           x="insurance_losses",
           y="premiums",
           row="Region")

# Show the plot
plt.show()
