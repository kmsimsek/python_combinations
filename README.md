# python_combinations
I'm new in programming and trying to make some practice. As a practice I try to develop a module that can generates combinations of a list. Also, it will give specific combinations which you are looking for. 

Idea is following;
You can give a list to the program. 
It can include any valid data types inside it.
Let's say it include n # of items inside.
We have possible combinations between 1 item and n items.

sample_list = [1,2,3]
to create combinations of this sample_list we need write following;

combinations(sample_list)

out put will be:
[[1,2,3], [1,2], [2,3], [1,3], 1, 2, 3]

You can add special conditions listed below;
1) min_item= (Minimum # of Item) 
  You can choose combinations that only have specific amount of item.
  For example for sample_list if we identify minimum number as 2.
  Comment for this is following;
  
  combinations(sample_list,min_item=[2])
  
  output will be:
  [[1,2,3], [1,2], [2,3], [1,3]]

2) max_item= (Maximum # of item)
  Just similar with min_item, you can identify max_item
  
  combinations(sample_list,max_item=[2])
  
  output will be:
  [[1,2], [2,3], [1,3], 1, 2, 3]
  
  you can use combined like following;
  
  combinations(sample_list, min_item=[2], max_item=[2]
  
  output will be:
  [[1,2], [2,3], [1,3]]
  
3) must_all=
  If you are looking for combinations of a list with given sub list must include all together in all returned combinations.
  For example if you are looking for all combinations of sample_list which include both 2 and 3
  
  combinations(sample_list,must_all=[2,3])
  
  output will be:
  [[1,2,3],[2,3]]
  
4) none_any=
  If you are looking for combinations of a list which does not include any of specific items.
  For example if we do not want to have 1 in combinations for sample list
  
  combinations(sample_list,none_any=[1])
  
  output will be:
  [[2,3]]
  
5) must_any=
  If you have a sub list which includes items that at least one of them must be in the combinations then you can use must_any= feature.
  
  sample_list_2 = [1,2,3,4]
  
  If we want to have 1 either 3 in all combinations ıf sample_list_2. You should use:
  combinations(sample_list_2,must_any=[1,3])
  
  output will be:
  
  [[1, 2, 3, 4], [2, 3, 4], [3, 4], [3], [2, 3], [1, 3, 4], [1, 4], [1], [1, 3], [1, 2, 4], [1, 2], [1, 2, 3]]
  
6) none_together=
  If we have a sub list that we do not want to have them together in the combinations than we need to use none_together=
  
  For example; if we don't want to have 1 and 3 together but they can be in combinations.
  
  combinations(sample_list_2,none_together=[1,3])
  
  output will be:
  [[2, 3, 4], [3, 4], [4], [3], [2, 4], [2], [2, 3], [1, 4], [1], [1, 2, 4], [1, 2]]
  
7) sum=
  sum= feature can be use to identify specific value or you can define a range as well.
  If list includes any item otherthan integer or float, program will eliminate them.
  
  you can use 
  (n1 and n2 are integer and/or float)
  (mark defines any of "=",">=",">","<","<="  -  including quotation marks):
  sum=[n1] ** working
  sum=[mark,n1] ** working
  sum=[mark,n1,mark,n2] ** still try to solve bug here
  
  for example:
  combinations(sample_list_2,sum=[">=",7])
  
  output will be:
  [[1, 2, 3, 4], [2, 3, 4], [3, 4], [1, 3, 4], [1, 2, 4]]

8) multiply=
  multiply= feature works similar to sum= feature
  
  you can use 
  (n1 and n2 are integer and/or float)
  (mark defines any of "=",">=",">","<","<="  -  including quotation marks):
  multiply=[n1] ** working
  multiply=[mark,n1] ** working
  multiply=[mark,n1,mark,n2] ** still try to solve bug here
  
  for example:
  combinations(sample_list_2,multiply=[">=",7])
  
  output will be:
  [[1, 2, 3, 4], [2, 3, 4], [3, 4], [2, 4], [1, 3, 4], [1, 2, 4]]
