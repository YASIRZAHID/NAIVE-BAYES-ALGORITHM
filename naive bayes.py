import numpy as np
import math

petal_length1 = [1.2, 2.3, 3.1, 1.8, 2.5]
petal_length2 = [0.9, 1.5, 2.1, 1.7, 2.0]
petal_length3 = [1.1, 1.9, 2.8, 1.6, 2.2]
petal_length4 = [1.5, 2.2, 2.9, 1.4, 1.8]

petal_width1 = [0.3, 0.4, 0.2, 0.5, 0.4]
petal_width2 = [0.2, 0.3, 0.5, 0.4, 0.3]
petal_width3 = [0.4, 0.2, 0.3, 0.6, 0.5]
petal_width4 = [0.3, 0.5, 0.4, 0.2, 0.3]

sepal_length1 = [5.1, 5.8, 6.0, 5.4, 6.2]
sepal_length2 = [4.9, 5.7, 6.2, 5.5, 6.7]
sepal_length3 = [5.0, 5.5, 6.3, 5.6, 6.4]
sepal_length4 = [4.8, 5.9, 6.4, 5.7, 6.3]

sepal_width1 = [3.5, 3.0, 3.2, 3.1, 2.8]
sepal_width2 = [3.0, 2.8, 3.1, 2.9, 3.1]
sepal_width3 = [3.6, 3.1, 3.4, 3.0, 3.2]
sepal_width4 = [3.1, 2.7, 3.3, 3.2, 2.9]

# Ask for user input
petal_length = input("Enter petal length value: ")
petal_width = input("Enter petal width value: ")
sepal_length = input("Enter sepal length value: ")
sepal_width = input("Enter sepal width value: ")


# Convert input string to list of floats
petal_length = [float(x) for x in petal_length.split()]
petal_width = [float(x) for x in petal_width.split()]
sepal_length = [float(x) for x in sepal_length.split()]
sepal_width = [float(x) for x in sepal_width.split()]

petal_length1_mean = 0;
petal_length2_mean = 0;
petal_length3_mean = 0;
petal_length4_mean = 0;

petal_width1_mean = 0;
petal_width2_mean = 0;
petal_width3_mean = 0;
petal_width4_mean = 0;

sepal_length1_mean = 0;
sepal_length2_mean = 0;
sepal_length3_mean = 0;
sepal_length4_mean = 0;

sepal_width1_mean =0;
sepal_width2_mean =0;
sepal_width3_mean =0;
sepal_width4_mean =0;

petal_length1_variance = 0;
petal_length2_variance = 0;
petal_length3_variance = 0;
petal_length4_variance = 0;

petal_width1_variance = 0;
petal_width2_variance = 0;
petal_width3_variance = 0;
petal_width4_variance = 0;

sepal_length1_variance = 0;
sepal_length2_variance = 0;
sepal_length3_variance = 0;
sepal_length4_variance = 0;

sepal_width1_variance =0;
sepal_width2_variance =0;
sepal_width3_variance =0;
sepal_width4_variance =0;

petal_length1_probability = 0;
petal_length2_probability = 0;
petal_length3_probability = 0;
petal_length4_probability = 0;

petal_width1_probability = 0;
petal_width2_probability = 0;
petal_width3_probability = 0;
petal_width4_probability = 0;

sepal_length1_probability = 0;
sepal_length2_probability = 0;
sepal_length3_probability = 0;
sepal_length4_probability = 0;

sepal_width1_probability =0;
sepal_width2_probability =0;
sepal_width3_probability =0;
sepal_width4_probability =0;

array_length = len(petal_length1)


for length in range(array_length):
    petal_length1_mean = petal_length1_mean + petal_length1[length-1];
    petal_length2_mean = petal_length2_mean + petal_length2[length-1];
    petal_length3_mean = petal_length3_mean + petal_length3[length-1];
    petal_length4_mean = petal_length4_mean + petal_length4[length-1];
    
    petal_width1_mean = petal_width1_mean + petal_width1[length-1];
    petal_width2_mean = petal_width2_mean + petal_width2[length-1];
    petal_width3_mean = petal_width3_mean + petal_width3[length-1];
    petal_width4_mean = petal_width4_mean + petal_width4[length-1];
    
    sepal_length1_mean = sepal_length1_mean + sepal_length1[length-1];
    sepal_length2_mean = sepal_length2_mean + sepal_length2[length-1];
    sepal_length3_mean = sepal_length3_mean + sepal_length3[length-1];
    sepal_length4_mean = sepal_length4_mean + sepal_length4[length-1];
    
    sepal_width1_mean = sepal_width1_mean + sepal_width1[length-1];
    sepal_width2_mean = sepal_width2_mean + sepal_width2[length-1];
    sepal_width3_mean = sepal_width3_mean + sepal_width3[length-1];
    sepal_width4_mean = sepal_width4_mean + sepal_width4[length-1];
    
    

petal_length1_mean  = petal_length1_mean / array_length;
petal_length2_mean  = petal_length2_mean / array_length;
petal_length3_mean  = petal_length3_mean / array_length;
petal_length4_mean  = petal_length4_mean / array_length;

petal_width1_mean  = petal_width1_mean / array_length;
petal_width2_mean  = petal_width2_mean / array_length;
petal_width3_mean  = petal_width3_mean / array_length;
petal_width4_mean  = petal_width4_mean / array_length;

sepal_length1_mean  = sepal_length1_mean / array_length;
sepal_length2_mean  = sepal_length2_mean / array_length;
petal_length3_mean  = sepal_length3_mean / array_length;
sepal_length4_mean  = sepal_length4_mean / array_length;

sepal_width1_mean  = sepal_width1_mean / array_length;
sepal_width2_mean  = sepal_width2_mean / array_length;
sepal_width3_mean  = sepal_width3_mean / array_length;
sepal_width4_mean  = sepal_width4_mean / array_length;




for length in range(array_length):
    petal_length1_variance += (petal_length1[length-1] - petal_length1_mean) ** 2
    petal_length2_variance += (petal_length2[length-1] - petal_length2_mean) ** 2
    petal_length3_variance += (petal_length3[length-1] - petal_length3_mean) ** 2
    petal_length4_variance += (petal_length4[length-1] - petal_length4_mean) ** 2
    
    petal_width1_variance += (petal_width1[length-1] - petal_width1_mean) ** 2
    petal_width2_variance += (petal_width2[length-1] - petal_width2_mean) ** 2
    petal_width3_variance += (petal_width3[length-1] - petal_width3_mean) ** 2
    petal_width4_variance += (petal_width4[length-1] - petal_width4_mean) ** 2
    
    sepal_length1_variance += (sepal_length1[length-1] - sepal_length1_mean) ** 2
    sepal_length2_variance += (sepal_length2[length-1] - sepal_length2_mean) ** 2
    sepal_length3_variance += (sepal_length3[length-1] - sepal_length3_mean) ** 2
    sepal_length4_variance += (sepal_length4[length-1] - sepal_length4_mean) ** 2
    
    sepal_width1_variance += (sepal_width1[length-1] - sepal_width1_mean) ** 2
    sepal_width2_variance += (sepal_width2[length-1] - sepal_width2_mean) ** 2
    sepal_width3_variance += (sepal_width3[length-1] - sepal_width3_mean) ** 2
    sepal_width4_variance += (sepal_width4[length-1] - sepal_width4_mean) ** 2
    
petal_length1_variance = (petal_length1_variance /(array_length) )   
petal_length2_variance = (petal_length2_variance /(array_length) )  
petal_length3_variance = (petal_length3_variance /(array_length) )  
petal_length4_variance = (petal_length4_variance /(array_length) )  

petal_width1_variance = ( petal_width1_variance /(array_length) ) 
petal_width2_variance = ( petal_width2_variance /(array_length) ) 
petal_width3_variance = ( petal_width3_variance /(array_length) ) 
petal_width4_variance = ( petal_width4_variance /(array_length) ) 

sepal_length1_variance = (sepal_length1_variance /(array_length) )  
sepal_length2_variance = (sepal_length2_variance /(array_length) )  
sepal_length3_variance = (sepal_length3_variance /(array_length) )  
sepal_length4_variance = (sepal_length4_variance /(array_length) )  

sepal_width1_variance = ( sepal_width1_variance /(array_length) ) 
sepal_width2_variance = ( sepal_width2_variance /(array_length) ) 
sepal_width3_variance = ( sepal_width3_variance /(array_length) ) 
sepal_width4_variance = ( sepal_width4_variance /(array_length) ) 

petal_length1_probability = 0;
petal_length2_probability = 0;
petal_length3_probability = 0;
petal_length4_probability = 0;

petal_width1_probability = 0;
petal_width2_probability = 0;
petal_width3_probability = 0;
petal_width4_probability = 0;

sepal_length1_probability = 0;
sepal_length2_probability = 0;
sepal_length3_probability = 0;
sepal_length4_probability = 0;

sepal_width1_probability =0;
sepal_width2_probability =0;
sepal_width3_probability =0;
sepal_width4_probability =0;

petal_length1_probability =  ( (1/(2 * math.pi * petal_length1_variance)**0.5) * math.exp( (-(petal_length1_variance - petal_length1_mean) ** 2)/(2*petal_length1_variance)));
petal_length2_probability =  ( (1/(2 * math.pi * petal_length2_variance)**0.5) * math.exp( (-(petal_length2_variance - petal_length2_mean) ** 2)/(2*petal_length2_variance)));
petal_length3_probability =  ( (1/(2 * math.pi * petal_length3_variance)**0.5) * math.exp( (-(petal_length3_variance - petal_length3_mean) ** 2)/(2*petal_length3_variance)));
petal_length4_probability =  ( (1/(2 * math.pi * petal_length4_variance)**0.5) * math.exp( (-(petal_length4_variance - petal_length4_mean) ** 2)/(2*petal_length4_variance)));

petal_width1_probability =   ( (1/(2 * math.pi * petal_width1_variance )**0.5) * math.exp( (-(petal_width1_variance  - petal_width1_mean) ** 2)/(2*petal_width1_variance )));
petal_width2_probability =   ( (1/(2 * math.pi * petal_width2_variance )**0.5) * math.exp( (-(petal_width2_variance  - petal_width2_mean) ** 2)/(2*petal_width2_variance )));
petal_width3_probability =   ( (1/(2 * math.pi * petal_width3_variance )**0.5) * math.exp( (-(petal_width3_variance  - petal_width3_mean) ** 2)/(2*petal_width3_variance )));
petal_width4_probability =   ( (1/(2 * math.pi * petal_width4_variance )**0.5) * math.exp( (-(petal_width4_variance  - petal_width4_mean) ** 2)/(2*petal_width4_variance )));

sepal_length1_probability =  ( (1/(2 * math.pi * sepal_length1_variance)**0.5) * math.exp( (-(sepal_length1_variance - sepal_length1_mean) ** 2)/(2*sepal_length1_variance)));
sepal_length2_probability =  ( (1/(2 * math.pi * sepal_length2_variance)**0.5) * math.exp( (-(sepal_length2_variance - sepal_length2_mean) ** 2)/(2*sepal_length2_variance)));
sepal_length3_probability =  ( (1/(2 * math.pi * sepal_length3_variance)**0.5) * math.exp( (-(sepal_length3_variance - sepal_length3_mean) ** 2)/(2*sepal_length3_variance)));
sepal_length4_probability =  ( (1/(2 * math.pi * sepal_length4_variance)**0.5) * math.exp( (-(sepal_length4_variance - sepal_length4_mean) ** 2)/(2*sepal_length4_variance)));

sepal_width1_probability =   ( (1/(2 * math.pi * sepal_width1_variance )**0.5) * math.exp( (-(sepal_width1_variance  - sepal_width1_mean) ** 2)/(2*sepal_width1_variance )));
sepal_width2_probability =   ( (1/(2 * math.pi * sepal_width2_variance )**0.5) * math.exp( (-(sepal_width2_variance  - sepal_width2_mean) ** 2)/(2*sepal_width2_variance )));
sepal_width3_probability =   ( (1/(2 * math.pi * sepal_width3_variance )**0.5) * math.exp( (-(sepal_width3_variance  - sepal_width3_mean) ** 2)/(2*sepal_width3_variance )));
sepal_width4_probability =   ( (1/(2 * math.pi * sepal_width4_variance )**0.5) * math.exp( (-(sepal_width4_variance  - sepal_width4_mean) ** 2)/(2*sepal_width4_variance )));

probability1 = 0.25 * petal_length1_probability * petal_width1_probability * sepal_length1_probability * sepal_width1_probability;
probability2 = 0.25 * petal_length2_probability * petal_width2_probability * sepal_length2_probability * sepal_width2_probability; 
probability3 = 0.25 * petal_length3_probability * petal_width3_probability * sepal_length3_probability * sepal_width3_probability;
probability4 = 0.25 * petal_length4_probability * petal_width4_probability * sepal_length4_probability * sepal_width4_probability;

all_array = np.zeros(4);
all_array[0] = probability1;
all_array[1] = probability2;
all_array[2] = probability3;
all_array[3] = probability4;
 
all_array_sorted = np.sort(all_array);
max_val = all_array_sorted[3];

if max_val == probability1:
    print("flower 1");
elif max_val == probability2:
    print("flower 2");
elif max_val == probability3:
    print("flower 3");
elif max_val == probability4:
    print("flower 4");
            

