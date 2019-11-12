
from tkinter import *
import mysql.connector
from tkinter import ttk, messagebox

try:
    con = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='Softwarica@123',
        database='shankar'
    )
    cur = con.cursor()


except mysql.connector.Error as e:
    print(e)


class ankit:

    def add_info(self):
        try:
            ID_entry = self.EntryID.get()
            Fn_entry = self.EntryFname.get()
            Ln_entry = self.EntryLname.get()
            Dg_entry = self.EntryDegree.get()
            Add_entry = self.EntryAddress.get()
            Age_entry = self.EntryAge.get()
            Num_entry = self.EntryNumber.get()

            if not ID_entry or not Fn_entry or not Ln_entry or not Age_entry or not Dg_entry or not Add_entry or not Num_entry:
                messagebox.showinfo('Info', 'Fill all the entry boxes')
                return

            if Fn_entry.isdigit():
                messagebox.showinfo("Info","Invalid First Name")
                return

            elif Ln_entry.isdigit():
                messagebox.showinfo("Info","Invalid Last Name")
                return

            elif Add_entry.isdigit():
                messagebox.showinfo("Info","Invalid Address")
                return

            elif not ID_entry.isdigit():
                messagebox.showinfo("Info","Invalid Id.Enter number only.")
                return

            elif not Age_entry.isdigit():
                messagebox.showinfo("Info","Invalid Age.Enter number only")
                return

            elif not Num_entry.isdigit():
                messagebox.showinfo("Info","Invalid Phone number.Enter number only.")
                return

            elif len(Num_entry) <= 9:
                messagebox.showinfo("Info","Phone number is not long enough.")
                return

            query = ' insert into work values(%s,%s,%s,%s,%s,%s,%s);'
            values = (ID_entry, Fn_entry, Ln_entry, Dg_entry, Add_entry, Age_entry, Num_entry)
            cur.execute(query, values)
            print('1 row inserted')
            con.commit()
            self.clear()
            self.show()
        except mysql.connector.IntegrityError as error:
            if str(error)[0:4]=='1062':
                messagebox.showinfo('Info','Duplicate Id entry found.')

    def show(self):
        query = 'select * from work'
        cur.execute(query)
        rows = cur.fetchall()

        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())

        for row in rows:
            self.student_table.insert('', END, values=row)

    def clear(self):
        self.EntryID.delete(0, END)
        self.EntryFname.delete(0, END)
        self.EntryLname.delete(0, END)
        self.EntryDegree.delete(0, END)
        self.EntryAddress.delete(0, END)
        self.EntryAge.delete(0, END)
        self.EntryNumber.delete(0, END)

    def update(self):
        try:
            ID_entry = self.EntryID.get()
            Fn_entry = self.EntryFname.get()
            ln_entry = self.EntryLname.get()
            Dg_entry = self.EntryDegree.get()
            Add_entry = self.EntryAddress.get()
            Age_entry = self.EntryAge.get()
            Num_entry = self.EntryNumber.get()
            if not ID_entry or not Fn_entry or not ln_entry or not Age_entry or not Dg_entry or not Add_entry or not Num_entry:
                messagebox.showinfo('Info', 'Fill all the entry boxes')
                return

            if Fn_entry.isdigit():
                messagebox.showinfo("Info", "Invalid First Name")
                return

            elif ln_entry.isdigit():
                messagebox.showinfo("Info", "Invalid Last Name")
                return

            elif Add_entry.isdigit():
                messagebox.showinfo("Info", "Invalid Address")
                return

            elif not ID_entry.isdigit():
                messagebox.showinfo("Info", "Invalid Id.Enter number only.")
                return

            elif not Age_entry.isdigit():
                messagebox.showinfo("Info", "Invalid Age.Enter number only")
                return

            elif not Num_entry.isdigit():
                messagebox.showinfo("Info", "Invalid Phone number.Enter number only.")
                return

            elif len(Num_entry) <= 9:
                messagebox.showinfo("Info", "Phone number is not long enough.")
                return
            query = ' update work set  Fname=%s, Lname=%s, Degree=%s, Address=%s, Age=%s, Number=%s where ID=%s'
            values = (Fn_entry, ln_entry, Dg_entry, Add_entry, Age_entry, Num_entry, ID_entry)
            cur.execute(query, values)
            con.commit()
            self.clear()
            self.show()
        except ValueError:
            messagebox.showinfo('Info','Fill every box')

    def pointer(self, event):
        try:
            point = self.student_table.focus()
            content = self.student_table.item(point)
            row = content['values']
            if len(row)!=0:
                self.clear()
                self.EntryID.insert(0, row[0])
                self.EntryFname.insert(0, row[1])
                self.EntryLname.insert(0, row[2])
                self.EntryDegree.insert(0, row[3])
                self.EntryAddress.insert(0, row[4])
                self.EntryAge.insert(0, row[5])
                self.EntryNumber.insert(0, row[6])
        except IndexError:
            pass

    def delete(self):
        try:
            selected_item = self.student_table.selection()
            self.student_table.delete(selected_item)

            query = 'delete from work where id=%s'
            id = self.EntryID.get()
            values = (id,)
            cur.execute(query, values)
            con.commit()
            self.clear()
        except:
            messagebox.showinfo('Info','Select data from table!')
    def search_algo(self, combo, find):
        try:
            if self.Search_With.get() == 'Fname':
                column = 1

            elif self.Search_With.get() == 'lname':
                column = 2

            elif self.Search_With.get() == 'Address':
                column = 4

            elif self.Search_With.get() == 'Age':
                column = 5
                find = int(find)

            elif self.Search_With.get() == 'Degree':
                column = 3

            elif self.Search_With.get() == 'ID':
                find = int(find)
                column = 0

            else:
                column = 6



            found_table = []
            for row in combo:
                if row[column] == find:
                    found_table.append(row)

            return found_table

        except ValueError:
            messagebox.showinfo('Info',"No valid data selected!")

    def searching(self):
        find = self.EntrySearch.get()
        aaa=self.Search_With.get()
        if not aaa:
            messagebox.showinfo('Info','No valid data found. Choose from option!')
        elif not find:
            messagebox.showinfo('Info','No value inserted!')
        else:
            query1 = " select * from work "
            cur.execute(query1)
            table = cur.fetchall()
            rows = self.search_algo(table, find)

            print(rows)
            if len(rows) != 0:
                self.student_table.delete(*self.student_table.get_children())

            for row in rows:
                self.student_table.insert('', END, values=row)

            if not rows:
                messagebox.showinfo('Info','No data found in database!')

            self.clear()


    def insertion_sort(self,arr,order):
        if order== 'Ascending':
            for i in range(1, len(arr)):
                key = arr[i]
                j = i - 1
                while j >= 0 and key < arr[j]:
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key

            return arr
        elif order=='Descending':
            for i in range(1, len(arr)):
                key = arr[i]
                j = i - 1
                while j >= 0 and key > arr[j]:
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key

            return arr

    def sorting(self):
        try:
            querys=" select * from work"
            cur.execute(querys)
            table=cur.fetchall()
            a=self.Sort_with.get()
            if a == 'Descending':
                order= 'Descending'

            else:
                order='Ascending'

            rows = self.insertion_sort(table, order)

            if len(rows) != 0:
                self.student_table.delete(*self.student_table.get_children())

            for row in rows:
                self.student_table.insert('', END, values=row)

            con.commit()
            self.clear()

        except:
            messagebox.showinfo('Info','No value selected!')

    def __init__(self, root):
        self.root = root
        var = StringVar()
        # ==============Button frame=========
        self.form=Frame(self.root, bd=4, bg='Grey' ,relief=RIDGE)
        self.form.place(x=20, y=0, width=600, height=380)

        self.btn_frame = Frame(self.root, bd=4, bg='grey', relief=RIDGE)
        self.btn_frame.place(x=20, y=380, width=600, height=40)

        self.frame = Frame(self.root, bd=4,bg='light blue', relief=RIDGE)
        self.frame.place(x=20, y=440, width=600, height=150)

        table_frame = Frame(self.root, bd=4, bg='gray', relief=RIDGE)
        table_frame.place(x=20, y=590, width=600, height=200)

        # ==================Lable==================
        self.ID = Label(self.form, bg='grey',fg='#ffffff', font=('arial ', 12,'bold'), text='ID').grid(row=0, column=0, padx=15, pady=15)
        self.Fname = Label(self.form, bg='gray',fg='#ffffff',font=('arial', 12,'bold'), text='Fname').grid(row=1, column=0, padx=15, pady=15)
        self.lname = Label(self.form, bg='gray',fg='#ffffff',font=('arial', 12,'bold'), text='Lname').grid(row=2, column=0, padx=15, pady=15)
        self.degree = Label(self.form, bg='gray',fg='#ffffff',font=('arial', 12,'bold'), text='Degree').grid(row=3, column=0, padx=15, pady=15)
        self.address = Label(self.form, bg='gray',fg='#ffffff',font=('arial', 12,'bold'), text='Address').grid(row=4, column=0, padx=15, pady=15)
        self.age = Label(self.form, bg='gray',fg='#ffffff',font=('arial', 12,'bold'), text='Age').grid(row=5, column=0, padx=15, pady=15)
        self.number = Label(self.form, bg='gray',fg='#ffffff',font=('arial', 12,'bold'), text='Number').grid(row=6, column=0, padx=15, pady=15)
        self.sortby = Label(self.frame,font=('arial', 10,'bold'), text='Sort With').grid(row=0, column=0, padx=10, pady=15)
        self.searchlbl = Label(self.frame,font=('arial', 10,'bold'), text='Search With').grid(row=0, column=3, padx=10, pady=15)
        self.searchby = Label(self.frame,font=('arial', 10,'bold'), text='Search Text').grid(row=1, column=3, padx=10, pady=15)

        # ================entry================
        self.EntryID = Entry(self.form)
        self.EntryID.grid(row=0, column=1, padx=15, pady=15)
        self.EntryFname = Entry(self.form)
        self.EntryFname.grid(row=1, column=1, padx=15, pady=15)
        self.EntryLname = Entry(self.form)
        self.EntryLname.grid(row=2, column=1, padx=15, pady=15)
        self.EntryAddress = Entry(self.form)
        self.EntryAddress.grid(row=4, column=1, padx=15, pady=15)
        self.EntryAge = Entry(self.form)
        self.EntryAge.grid(row=5, column=1, padx=15, pady=15)
        self.EntryNumber = Entry(self.form)
        self.EntryNumber.grid(row=6, column=1, padx=15, pady=15)
        self.EntrySearch = Entry(self.frame)
        self.EntrySearch.grid(row=1, column=4, padx=15, pady=15)

        # ==========optionbox=========
        self.Sort_with = ttk.Combobox(self.frame, font=('arial', 10), state='readonly')
        self.Sort_with['values'] = ('Ascending', 'Descending')
        self.Sort_with.grid(row=0, column=1, pady=10, padx=20)

        self.Search_With = ttk.Combobox(self.frame, font=('arial', 10), state='readonly')
        self.Search_With['values'] = ('Fname', 'lname', 'Address', 'Age', 'Degree', 'ID', 'Number')
        self.Search_With.grid(row=0, column=4, pady=10, padx=20)

        self.EntryDegree = ttk.Combobox(self.form,font=('arial', 10),width=15)
        self.EntryDegree['values']=('BSc (Hons)Computing','BSc (Hons)Ethical Hacking & Cybersecurity')
        self.EntryDegree.grid(row=3, column=1, padx=15, pady=15)
        # =================Buttons================
        self.button = Button(self.btn_frame, text='Add', command=self.add_info, width=10, height=1).grid(row=7,
                                                                                                         column=0,
                                                                                                         padx=35)
        self.button1 = Button(self.btn_frame, text='update', command=self.update, width=10, height=1).grid(row=7,
                                                                                                           column=1,
                                                                                                           padx=35)
        self.button2 = Button(self.btn_frame, text='Delete', command=self.delete, width=10, height=1).grid(row=7,
                                                                                                           column=2,
                                                                                                           padx=35)
        self.button3 = Button(self.btn_frame, text='Clear', command=self.clear, width=10, height=1).grid(row=7,
                                                                                                         column=3,
                                                                                                         padx=35)

        self.button4 = Button(self.frame, text='Search',font=('arial 10 bold'), command=self.searching, width=10, height=1).grid(row=2,
                                                                                                         column=4,
                                                                                                         padx=15)
        self.button5 = Button(self.frame, text='Sort',font=('arial 10 bold'), command=self.sorting, width=10, height=1).grid(row=2,
                                                                                                        column=1,
                                                                                                        padx=15)


        # =========scrollbar=======
        self.scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        self.scroll_y = Scrollbar(table_frame, orient=VERTICAL)

        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)




        # ==============table=================
        self.student_table = ttk.Treeview(table_frame,
                                          column=('id', 'fname', 'lname', 'deg', 'address', 'age', 'number'),
                                          xscrollcommand=self.scroll_x.set,yscrollcommand=self.scroll_y.set)

        self.student_table.heading('id', text='ID')
        self.student_table.heading('fname', text='Fname')
        self.student_table.heading('lname', text='Lname')
        self.student_table.heading('deg', text='Degree')
        self.student_table.heading('address', text='Address')
        self.student_table.heading('age', text='Age')
        self.student_table.heading('number', text="Number")
        self.student_table['show'] = 'headings'
        self.student_table.pack()

        self.student_table.column('id', width=60)
        self.student_table.column('fname', width=80)
        self.student_table.column('lname', width=80)
        self.student_table.column('deg', width=150)
        self.student_table.column('address', width=80)
        self.student_table.column('age', width=60)
        self.student_table.column('number', width=70)

        self.scroll_x.config(command=self.student_table.xview)
        self.scroll_y.config(command=self.student_table.yview)

        self.show()

        self.student_table.bind('<ButtonRelease-1>', self.pointer)

        self.student_table.pack(fill=BOTH, expand=True)



form = Tk()
aaa=ankit(form)
form.title('Student Management System ')
form.geometry('650x750')
form.resizable(False,False)
form.mainloop()
