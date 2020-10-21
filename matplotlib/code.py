# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(path, sep = ',', delimiter = None)
loan_status = data['Loan_Status'].value_counts()
loan_status.plot(kind="bar")
plt.show()
#Code starts here


# --------------
#Code starts here

property_and_loan = data.groupby(['Property_Area','Loan_Status']).size().unstack()

property_and_loan.plot(kind='bar', stacked=False, figsize=(15,10))
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
plt.show()


# --------------
#Code starts here

education_and_loan = data.groupby(['Education' , 'Loan_Status']).size().unstack()

education_and_loan.plot(kind='bar', stacked=False, figsize=(15,10))

plt.xlabel('Education Status')
plt.ylabel('Loan Status ')
plt.xticks(rotation=45)
plt.show()


# --------------
#Code starts here
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
graduate = data[data['Education'] == 'Graduate']
 #df[df['Type 1'] == 'Electric']
not_graduate = data[data['Education'] == 'Not Graduate']

graduate['LoanAmount'].plot(kind='density', label='Graduate')
not_graduate['LoanAmount'].plot(kind='density',label='Not Graduate')








#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
fig, (ax_1, ax_2, ax_3) = plt.subplots(1,3, figsize=(20,10))

ax_1.scatter(data['ApplicantIncome'],data["LoanAmount"])
ax_2.scatter(data['CoapplicantIncome'],data["LoanAmount"])

data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']
ax_3.scatter(data['TotalIncome'],data["LoanAmount"])






