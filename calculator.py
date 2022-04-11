#Main program file
#CalculateBioIndex.py
#Date Last Modified: December, 2, 2021
#Authors: Kira-Marie Lazda, Shawn Ryan, Kathleen Soodhoo, Jing Wang 

# The purpose of this program is to calculate Simpsons and/or Shannons index. 
# Shannons index accounts for species richness as well as eveness. The higher these values are 
# the greater the biodiversity of the site is. 
# Simpsons index accounts more for species dominance, meaning populations having higher numbers 
# will result in a higher esimate of diversity. 
# References for the formulas and background for these indices come from : 
#  https://www.omnicalculator.com/ecology/shannon-index
#  https://www.omnicalculator.com/statistics/simpsons-diversity-index
#  http://www.tiem.utk.edu/~gross/bioed/bealsmodules/shannonDI.html
#  http://www.countrysideinfo.co.uk/simpsons.htm

# This program recieves values either through manual user input or by having the user choose between 
# two locations that have data sets already associated with them. The program also asks the user to 
# choose which indices they want to be calculated. 
# The output of this program are the calculated index values to a single csv file that shows the user 
# the final results of the calculation as well as the values used to calculate them. 

# This program assumes that the data provided by the user is accurate and in the form of comma delineated 
# integers as requested. It also assumes that the format of the output, in a csv file, is suitable for their needs 
# The format of this output is also recoginized as a limitation as it provides less allowance for manipulation 
# in more complicated ways such as being appended to a database where there is more  opportunity for analysis. 
# This program also limits the user to working with data at two locations if they choose the file input.

#Contribution Statements: 
#   Kira-Marie Lazda: Manual Input function, Main function, provided txt files for file input option
#   Shawn Ryan: Shannon Index function
#   Kathleen Soodhoo: Top of code documentation, Test Values table, Simpsons Index Function 
#   Jing Wang: File Input function, helped with file output section of main function



def Shannon_Index(speciesData):
    #Code by Shawn
    import math
    total = sum(speciesData)
    result = 0
    for value in speciesData:
#   pi is the proportion of i-th species in a whole community. 
#   value is the individuals of a given type/species.
#   total is the total number of individuals in a community. 
#   Calculating the proportion: Divide the number of individuals in a species by the total number of individuals in the community. 
        pi = value / total
#   For each species, multiply the proportion by the logarithm of the proportion and sum them.         
        result += pi * math.log(pi)
#   Multiply the result by -1 to calculate the Shannon Index
    ShannonIndex = (-1)*result
#   Calculating the Shannon Equitability.
    EquitabilityIndex = ShannonIndex/math.log(len(speciesData))
    return ShannonIndex, EquitabilityIndex


def Simpson_Index(speciesData):
    #code by Kathleen
    import math 

    #Inital check to make sure there are at least 2 inputs which is required for this index 
    #If there are not at least 2 species, the output file will receive "N/A" as the result for Simpson's Index
    #Note: this should not ever happen because the input functions ensure at least two values are being passed here
    if len(speciesData) < 2:
        SimpsonsResults = "N/A - Need more than 2 values to compute Simpson's Index"
    
    else:
        #Get the sum of the total population 
        TotalIndividuals = sum(speciesData)
        #Get the total number of observations using the sum 
        N = TotalIndividuals*(TotalIndividuals-1)
        niSum = 0
        # loop through through the list of values 
        for i in range(len(speciesData)):
        #find the population size of each species 
            IndivPerSpecies= speciesData[i]
            #calculate (ni*ni-1) for each species and assign it to the variable ni
            ni =(IndivPerSpecies*(IndivPerSpecies-1))
            #increase niSum by ni for each species
            niSum+=ni
        #calculate Simpsons Index 
        SimpsonsResults = 1-(niSum/N)
    return SimpsonsResults 

def Manual_Input():
    """Manual_Input function is called from the main function when the user chooses option 'M' for the data entry choice.
        Inputs: none
        Purpose: asks the user for a comma-separated list of values representing the number of individuals per species.
        Returns: a cleaned list of the inputted data ('listData'), where each item in the list is a float greater than zero."""

    #Display the user's choice of manual data entry and provide an example of the correct format for entry.   
    print()
    print('You chose to input the data manually.')
    print('         Please enter the positive, non-zero integer number of individuals per species separated by commas.')
    print('         For example: 1,15,67,3,30,15')
    print()
    print("**Note: a minimum of two values is required to calculate the indices.")
    print()
    # create a variable to control the while loop
    userinput = 'invalid'
    # prompt the user for their species data until they enter at least one value.
    while userinput=='invalid':
        inputData = input('Enter your comma-separated data here: ')
        if len(inputData) >0:                               #checks to make sure the input is not an empty string
            try:
                if ',' in inputData:                        #if there are commas in the input string, split the string into a list of values delimited by commas
                    listData = inputData.split(',')
                    for i in range(len(listData)):          #iterate through the new list and convert every item to a float
                        listData[i] = float(listData[i])                    
                    finalData = listData[:]                 #create a list that will hold the final cleaned data
                    for item in listData:                   #iterate through the listData to look for any negative values
                        if item<=0:
                            finalData.remove(item)          #remove any negative or zero values from the final data list - notify user that they are not valid values for species data
                            print('You have provided a negative value in your list of data:'+str(item)+'. It has been removed prior to calculations being made.')
                    if len(finalData) >=2:                  #checks to see if finalData is not an empty list after any invalid values were removed
                        userinput = 'valid'                 #set the loop variable to 'valid' to exit the while loop
                    else:
                        print('You entered too many invalid values. Please try again with at least two positive, non-zero values.')  #if the user entered only invalid values, prompt them to try again  
                elif ' ' in inputData:
                    print('You forgot to separate your data with commas! Please try again.')                        #if there are spaces instead of commas in the input string, prompt user to try again
                else:
                    print('You only entered one value. A minimum of two values is required to calculate the indices. Please try again.')
                #     listData = [float(inputData)]                                                                   #if user only entered one value, check to make sure it is a non-zero, positive number
                #     finalData = listData[:]
                #     if finalData[0]<=0:
                #         print('You entered a single value less than or equal to zero. Please try again.')           #prompt them to try again if their single value was invalid
                #     else:
                #         userinput = 'valid'                                                                         #set the loop variable to 'valid' to exit the while loop if their entry is valid 
            except(ValueError):
                print('One or more of your entered values is not a number. Please enter numbers separated by commas only!') #catch any values that cannot be converted to float
        else:                                                                                                       #if the input is an emptry string, prompt the user to re-enter their data.
            print('You forgot to enter your data! Please try again.')
    return finalData

def File_Input(siteChoice):
    #Code by Jing Wang

    #initializing filename as empty list
    filename = ''
    file_A = 'LindsaySpecies.txt'
    file_B = 'SquamishSpecies.txt'
    # A is for LindsaySpecies.txt, B is for SquamishSpecies.txt
    if siteChoice.capitalize() == 'A':
        filename = file_A
    elif siteChoice.capitalize() == 'B':
        filename = file_B
    
    
    #initializing data list.
    data = []
    speciesNames = []
    #Try opening file to read
    try:
        f1 = open(filename, 'r')    #Open the file to read, if it opens, i means the file is there.
        filedata = f1.readlines()   #readlines() reads all the lines
        f1.close                    #close the file
    except(FileNotFoundError):          #This exception is for if the file is not in directory, main() will terminate
        print("WARNING!")
        print(filename," not found in directory, please make sure it's there")  
        speciesNames = "Invalid"        
        data = "Invalid"                #Load data and speciesName as "Invalid" to trigger a termination in Main()
        return speciesNames, data       #Return and terminate function.
    
    #print(filedata)
    #loading the second column into data list, with each elements as float
    #print(filedata)
    if len(filedata) > 0:
        c = 0           #total count of omitted lines
        l = []          #all the lines that are omitted for every reasons, only lines with missing or invalid population data are omitted
        mspnl = []      #for lines that have missing/empty specie names
        mcl = []        #for lines that are missing comma
        mdl = []        #for original file lines that has missing or invalid population data
        for i in range(len(filedata)): 
            if ',' in filedata[i]:                          #this if statement picks only the lines with a comma in it.
                templine = filedata[i].strip()                  #Strips leading and trailing unuseful chars and load it in templine
                tempspecies = templine.split(",")[0].strip()    #Split the line by comma and strip the first element and load it in tempspecies
                tempdata = templine.split(",")[1].strip()       #Split the line by comma and strip the second element and load it in tempdata
                #error handling for invalid population data:
                try:
                    tempdata = float(tempdata)              #try to convert population data from string to float
                    tempdata = round(tempdata,0)            #try to round population data in tempdata
                    data.append(tempdata)                   #if the the first 2 tries goes through, proceed to append tempdata to data
                    #loading specie name stored in tempspecies to speciesNames (output one).
                    if tempspecies != '':
                        speciesNames.append(tempspecies)    #if none empty then just append.
                    else:
                        mspnl.append(i)                     #if it is empty, record this line index
                        speciesNames.append('N/A')          #Put down "N/A" in specieNames (output one)
                except(ValueError):             #this exception is handles lines with invalid population data input, that include non-numeric entries and empty entries
                    mdl.append(i)               #record this line in mdl, aka the list of lines with missing/invalid populattion data        
                    l.append(i)                 #record this line in l, aka the list of lines omitted
                    c = c+1                     #increment total count of omitted lines
            else:                           #lines without comma:
                mcl.append(i)               #record this line in mcl, aka the list of lines with missing comma.
                l.append(i)                 #record this line in l, aka the list of lines omitted
                c = c+1                     #increment total count of omitted lines
        if c == len(filedata):              #This condition is for a failure to load any useful data because every line is no good, main() will terminate.
            #displaying warning report
            print(" --------- WARNING REPORT ---------")
            print(filename, " does not have any useful data to load")
            print("of the ", len(filedata), "lines in the file, all of them are omitted.")
            if len(mdl)>0: print("Omitted line(s) ", mdl," has/have missing or invalid population data")
            if len(mcl)>0: print("Omitted line(s) ", mcl," has/have missing comma")
            speciesNames = "Invalid"
            data = "Invalid"
        elif c > 0:                     #This condition is for a failure to load some of the file data because some lines are no good, main() will NOT terminate.
            #displaying warning report
            print(" --------- WARNING REPORT ---------")
            print("of the ", len(filedata), "line(s) in the file, line(s) ", l, " are omitted.")
            if len(mdl)>0: print("Omitted line(s) ", mdl," has/have missing or invalid population data")
            if len(mcl)>0: print("Omitted line(s) ", mcl," has/have missing comma")
            if len(mspnl)>0: print("Line(s) ", mspnl, "have missing species name, thus filled in with 'N/A'.")
    else:                               #This condition is for an empty input file, main() will terminate
        print("WARNING!")
        print(filename, " is an empty file")
        speciesNames = "Invalid"
        data = "Invalid"
    return speciesNames, data

def main():
    """The main function displays the program's purpose, allows the user to choose what form of data entry they would like, 
        calls the Manual_Input or File_Input function depending on their choice, and give users the options of indices to calculate.
        The function outputs a csv file with the results."""
    #display the program purpose and information about biodiversity indices.
    print('This program helps identify the diversity level of an ecological community.')
    print()
    print('The species data for your chosen community can be used to calculate two biodiversity indices and species evenness.')
    print()
    print('Biodiversity indices produce comparable measures of biodiversity in and across animal communities using species data at a given location.') 
    print('     Shannon’s index is the most common diversity index as it accounts for both species richness (i.e. the number of different species present) and evenness (each species’ relative abundance)')
    print('     whereas Simpson’s index provides a species dominance estimate.')
    print("     Shannon's equitability score will also give a sense of how evenly the species are distributed in the ecological community."      )
    #display how and where the results will be saved
    print('The results will be saved to a csv file in this directory with a file name of your choice.')
    print()
    print()
    #display to the user their data entry options
    print('You must first supply species data for your site. Here are your input options:')
    print('     Option M: Manually enter your species data')
    print('     Option F: Use an existing file of species data for one of two predetermined sites')

    #set a variable to control the input while loop
    choice = 'invalid'
    #prompt the user for a data input choice until they provide a valid option
    while choice == 'invalid':
        dataInputChoice = input('Please enter your input choice (M of F):')
        if dataInputChoice.capitalize() == 'M':                                                             #if the user selects 'M', call the Manual_Input function
            data = Manual_Input()                                                                           #the function return is assigned to the variable 'data'
            print('Here is your final list of data: ', data)
            choice = 'valid'                                                                                #change the choice variable to valid to break out of the while loop
        elif dataInputChoice.capitalize() == 'F':
            print('You must first choose which ecological site you would like to access the data for.')     #if the user selects 'F', ask the user which site they want the data for
            print('Here are your site options:')
            print('         Option A: Lindsay, Ontario')
            print('         Option B: Squamish, British Columbia')
            print()

            #set a variable to control the input while loop
            filechoice = 'invalid'
            #prompt the user for a site choice until they provide a valid option
            while filechoice == 'invalid':
                site = input('Please enter your site choice (A or B): ')
                #change the variable filechoice to 'valid' only if the user selects option A or B as 'site'
                if site.capitalize() == 'A':
                    print('You chose to use a file of existing data for site A - Lindsay')
                    filechoice = 'valid'
                elif site.capitalize() == 'B':
                    print('You chose to use a file of existing data for site B - Squamish')
                    filechoice = 'valid'
                else:
                    print('You did not enter a valid site option. Please try again.')
            #call the function File_Input with site as the parameter
            species, data = File_Input(site)                                                                #the function returns a tuple containing the species names and data
            #the following code will deal with file input problem like specified in Warning Report: 
            if species == "Invalid" and data == "Invalid":
                print("failed to load file data, please refer to Warning Report for details")
                print("Program terminating...")
                return 0
            choice = 'valid'
        else:
            print('You did not enter a valid input option. Please try again.')
    
    #Display to the user the various biodiversity index options the program can calculate
    print()
    print('Here are the available biodiversity index calculation options:')
    print("         Option 1: Calculate Shannon's Diversity Index")
    print("         Option 2: Calculate Simpson's Diversity Index")
    print("         Option 3: Calculate both Shannon's and Simpson's Diversity Indices")
    print()
    
    #set a variable to control the input while loop
    bioChoice = 'invalid'
    #prompt the user for a calculation option until they provide one of the three valid choices
    while bioChoice == 'invalid':
        indexChoice = input('Please enter your biodiversity index choice (1,2 or 3): ')
        try:
            if int(indexChoice) > 3 or int(indexChoice) < 1:
                print('You did not enter a valid biodiversity index option. Please try again.')
            else:
                print('You have chosen option ' + indexChoice)
                if int(indexChoice) == 1:
                    ShannonResults = Shannon_Index(data)            #call Shannon_Index function using data as parameter if user selects option 1
                    #print(ShannonResults)
                elif int(indexChoice) == 2:
                    SimpsonResults = Simpson_Index(data)            #call Simpson_Index function using data as parameter if user selects option 2
                    #print(SimpsonResults)
                elif int(indexChoice) == 3:
                    ShannonResults = Shannon_Index(data)            #call both Shannon_Index and Simpson_Index functions using data as parameter if user selects option 3
                    SimpsonResults = Simpson_Index(data)
                    #print(ShannonResults, SimpsonResults)
                bioChoice = 'valid'                                 #set the loop variable to 'valid' to break out of the while loop
        except ValueError:
            print('You have not entered a number (1, 2 or 3). Please try again.')   #catch any ValueErrors that result from the user not entering a number

    print('Your biodiversity index results have been calculated!')
    
    #file output section
    import csv
    #create a variable to control the input while loop
    outName = 'invalid'
    #prompt the user to enter a file name for the calculated results until they enter a non-empty name
    while outName=='invalid':
        outputFileName = input('Please provide a file name for how you would like your file to be saved without the extension (i.e. BioIndexResults):')
        try:
            if len(outputFileName) >0:                                                      #checks if user entered a file name
                fileOut = open(outputFileName+'.csv', 'w', newline='')                      #open/create a csv file using that name for writing
                writer = csv.writer(fileOut)                                                #create a csv writer
                writer.writerow(['Results for Biodiversity Index Calculator'])
                if dataInputChoice.capitalize() == 'M':                                     #if the user had manually inputed data, write their data to the file with appropriate headings        
                    writer.writerow(['Species Label', 'Number of Individuals'])
                    counter = 1
                    for item in data:                                                       #since the user only supplies numbers and no species labels, create species labels using the counter variable
                        writer.writerow(['Species '+str(counter), item])
                        counter +=1
                if dataInputChoice.capitalize() == 'F':                                     #if the user had chosen a file of data, writer the original data to the file along with the chosen site identification
                    writer.writerow(['Data provided for site:', site.capitalize()])
                    writer.writerow(['Species Name', 'Number of Individuals'])
                    for i in range(len(species)):
                        writer.writerow([species[i], data[i]])
                
                #write the corresponding biodiversity index results to the file after the data depending on which index option the user chose
                if indexChoice == '1':
                    writer.writerow(['Shannon Diversity Index is:  ',round(ShannonResults[0], 3)])
                    writer.writerow(['Shannon Equitability is:  ',round(ShannonResults[1],3)])
                elif indexChoice == '2':
                    writer.writerow(['Simpson Diversity Index is:  ',round(SimpsonResults, 3)])
                elif indexChoice == '3':
                    writer.writerow(['Shannon Diversity Index is:  ',round(ShannonResults[0],3)])
                    writer.writerow(['Shannon Equitability is:  ',round(ShannonResults[1],3)])
                    writer.writerow(['Simpson Diversity Index is:  ',round(SimpsonResults,3)])
                
                outName='valid'                                                             #change the loop variable to valid to break out of the input while loop
            else:
                print('You forgot to enter a file name for your results. Please try again!')
        except PermissionError:                                                              #catch a permission error resulting from the user already having that file open in another program
            print('Cannot write to your chosen file because it is open in another program. Please close the file and try again.')
            print()

if __name__=="__main__":
    main()