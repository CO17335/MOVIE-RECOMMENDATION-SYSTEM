import pandas as pd
from scipy import sparse
from tkinter import *
from tkinter import ttk


mov =[]
rat =[]
res =[]

def on_keyrelease(event):
    
    # get text from entry
    value = event.widget.get()
    value = value.strip().lower()
    
    # get data from test_list
    if value == '':
        data = test_list
    else:
        data = []
        for item in test_list:
            if value in item.lower():
                data.append(item)                

    # update data in listbox
    listbox_update(data)
    
    
def listbox_update(data):
    # delete previous data
    listbox.delete(0, 'end')
    
    # sorting data 
    data = sorted(data, key=str.lower)

    # put new data
    for item in data:
        listbox.insert('end', item)


def on_select(event):
    # display element selected on list
    #print('(event) previous:', event.widget.get('active'))
    #print('(event)  current:', event.widget.get(event.widget.curselection()))
    #print('---')
    mov.append(event.widget.get(event.widget.curselection()))
    


  
def select():
    rat.append(var.get())

#view databsae 
def save_database():
    class Table:
        
        def __init__(self,root): 
          
        # code for creating table 
            for i in range(total_rows): 
                for j in range(total_columns): 
                  
                    self.e = Entry(v_database, width=40) 
                    self.e.grid(row=i, column=j) 
                    self.e.insert(END, lst[i][j])
                    
    res = list(zip(mov,rat))
    lst = res
    total_rows = len(lst) 
    total_columns = len(lst[0])
    t = Table(v_database)


def final_output():
    res = list(zip(mov,rat))
    action_lover = res
    similar_movies = pd.DataFrame()
    for movie,rating in action_lover:
        similar_movies = similar_movies.append(get_similar(movie,rating),ignore_index = True )

    similar_movies.head(10)
    final = (similar_movies.sum().sort_values(ascending=False).head(20))
    t1 = Text(recommendation) 
    t1.pack()
    df = pd.DataFrame(similar_movies.sum().sort_values(ascending=False).head(20)) 
    t1.insert('end', similar_movies.sum().sort_values(ascending=False).head(20))
    

    
    

ratings = pd.read_csv('dataset/ratings.csv')
movies = pd.read_csv('dataset/movies.csv')
m_name = pd.read_csv('dataset/item_similarity_df.csv')
ratings = pd.merge(movies,ratings).drop(['genres','timestamp'],axis=1)
print(ratings.shape)
ratings.head()

userRatings = ratings.pivot_table(index=['userId'],columns=['title'],values='rating')
userRatings.head()
print("Before: ",userRatings.shape)
userRatings = userRatings.dropna(thresh=10, axis=1).fillna(0,axis=1)
#userRatings.fillna(0, inplace=True)
print("After: ",userRatings.shape)

corrMatrix = userRatings.corr(method='pearson')
corrMatrix.head(100)

def get_similar(movie_name,rating):
    similar_ratings = corrMatrix[movie_name]*(rating-2.5)
    similar_ratings = similar_ratings.sort_values(ascending=False)
    #print(type(similar_ratings))
    return similar_ratings

romantic_lover = [("(500) Days of Summer (2009)",5),("Alice in Wonderland (2010)",3),("Aliens (1986)",1),("2001: A Space Odyssey (1968)",2)]
similar_movies = pd.DataFrame()
for movie,rating in romantic_lover:
    similar_movies = similar_movies.append(get_similar(movie,rating),ignore_index = False)

similar_movies.head(10)



test_list = m_name['title']


root = Tk()


#crating tabs
my_notebook = ttk.Notebook(root)
my_notebook.pack()

c_database = Frame(my_notebook)
v_database = Frame(my_notebook)
recommendation = Frame(my_notebook)



#recommendation

c_database.pack(fill = "both", expand=1)
v_database.pack(fill = "both", expand=1)
recommendation.pack(fill = "both", expand=2)

my_notebook.add(c_database, text = "CREATE DATABASE")
my_notebook.add(v_database, text = "VIEW DATABASE")
my_notebook.add(recommendation, text = "RECOMMENDATION ")

#creat database
sel_label = Label(c_database, text ="  SELECT MOVIE  ").grid(row=1 , column=0)

entry = Entry(c_database)
entry.grid(row=1 , column=1)
entry.bind('<KeyRelease>', on_keyrelease)

listbox = Listbox(c_database)
listbox.grid(row=2 , column=1)
#listbox.bind('<Double-Button-1>', on_select)
listbox.bind('<<ListboxSelect>>', on_select)
listbox_update(test_list)
 
star_label = Label(c_database , text = "  GIVE RATING  ").grid(row=5 , column=0)

var= IntVar()
R1 = Radiobutton(c_database, text="1", variable=var, value=1 , command=select).grid(row=3, column=1)
R2 = Radiobutton(c_database, text="2", variable=var, value=2, command=select).grid(row=4, column=1)
R3 = Radiobutton(c_database, text="3", variable=var, value=3, command=select).grid(row=5, column=1)
R4 = Radiobutton(c_database, text="4", variable=var, value=4, command=select).grid(row=6, column=1)
R5 = Radiobutton(c_database, text="5", variable=var, value=5, command=select).grid(row=7, column=1)

s_db_button = Button(c_database ,text="SAVE DATABASE", command=save_database).grid(row=8,column=0)

recommend = Button(c_database ,text="RECOMMEND MOVIES", command=final_output).grid(row=8,column=1)






root.mainloop()


print(mov)
print(rat)


print(res)

"""
action_lover = res
similar_movies = pd.DataFrame()
for movie,rating in action_lover:
    similar_movies = similar_movies.append(get_similar(movie,rating),ignore_index = False )

similar_movies.head(10)
final = (similar_movies.sum().sort_values(ascending=False).head(20))


print(list(final))

"""
