import tkinter as tk
from tkinter import messagebox, ttk
import psycopg2
from psycopg2 import OperationalError

def create_connection():
    try:
        connection = psycopg2.connect(
            host="localhost", 
            dbname="activities2",
            user="myuser",
            password="123",
            port=5433
        )
        return connection
    except OperationalError as e:
        print("Ошибка при подключении:", e)
        return None
    
def insert_movie():
    title = entry_movie_title.get()
    genre = entry_movie_genre.get()
    watch_date = entry_movie_date.get()
    
    conn = create_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute(
                "SELECT insert_into_movies(%s, %s, %s)",
                (title, genre, watch_date)
            )
            conn.commit()
            messagebox.showinfo("Успех", "Данные успешно вставлены")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
        finally:
            cur.close()
            conn.close()


def insert_poolvisit():
    club_name = entry_pool_name.get()
    duration = entry_pool_duration.get()
    visit_date = entry_pool_date.get()
    
    conn = create_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute(
                "SELECT insert_into_poolvisits(%s, %s, %s)",
                (club_name, duration, visit_date)
            )
            conn.commit()
            messagebox.showinfo("Успех", "Данные успешно вставлены")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
        finally:
            cur.close()
            conn.close()


def insert_walk():
    friend_name = entry_walk_friend_name.get()
    duration = entry_walk_duration.get()
    walk_date = entry_walk_date.get()
    
    conn = create_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute(
                "SELECT insert_into_walks(%s, %s, %s)",
                (friend_name, duration, walk_date)
            )
            conn.commit()
            messagebox.showinfo("Успех", "Данные успешно вставлены")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
        finally:
            cur.close()
            conn.close()


def check_activity():
    conn = create_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM get_all_dailyactivities()")
            rows = cur.fetchall()
            
            # Очистить окно таблицы
            for i in tree_movies.get_children():
                tree_movies.delete(i)

            # Отобразить данные
            for row in rows:
                tree_movies.insert("", tk.END, values=row)

        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
        finally:
            cur.close()
            conn.close()




root = tk.Tk()
root.title("Учет активности студентов")
root.geometry("700x800")


# Вставка данных (формы для ввода)
frame_insert_movie = tk.Frame(root)
frame_insert_movie.pack(pady=10, padx=1)

tk.Label(frame_insert_movie, text="Название:").grid(row=0, column=0)
entry_movie_title = tk.Entry(frame_insert_movie)
entry_movie_title.grid(row=0, column=1)

tk.Label(frame_insert_movie, text="Жанр:").grid(row=1, column=0)
entry_movie_genre = tk.Entry(frame_insert_movie)
entry_movie_genre.grid(row=1, column=1)

tk.Label(frame_insert_movie, text="Дата просмотра (ГГГГ-ММ-ДД):").grid(row=2, column=0)
entry_movie_date = tk.Entry(frame_insert_movie)
entry_movie_date.grid(row=2, column=1)

btn_insert = tk.Button(frame_insert_movie, text="Вставить фильм", command=insert_movie)
btn_insert.grid(row=3, columnspan=2, pady=10)




frame_insert_walks = tk.Frame(root)
frame_insert_walks.pack(pady=10)

tk.Label(frame_insert_walks, text="Имя друга:").grid(row=0, column=0)
entry_walk_friend_name = tk.Entry(frame_insert_walks)
entry_walk_friend_name.grid(row=0, column=1)

tk.Label(frame_insert_walks, text="Длительность").grid(row=1, column=0)
entry_walk_duration = tk.Entry(frame_insert_walks)
entry_walk_duration.grid(row=1, column=1)

tk.Label(frame_insert_walks, text="Дата прогулки (ГГГГ-ММ-ДД):").grid(row=2, column=0)
entry_walk_date = tk.Entry(frame_insert_walks)
entry_walk_date.grid(row=2, column=1)

btn_insert = tk.Button(frame_insert_walks, text="Вставить прогулку", command=insert_walk)
btn_insert.grid(row=3, columnspan=2, pady=10)




frame_insert_poolvisit = tk.Frame(root)
frame_insert_poolvisit.pack(pady=10)

tk.Label(frame_insert_poolvisit, text="Название клуба:").grid(row=0, column=0)
entry_pool_name = tk.Entry(frame_insert_poolvisit)
entry_pool_name.grid(row=0, column=1)

tk.Label(frame_insert_poolvisit, text="Длительность:").grid(row=1, column=0)
entry_pool_duration = tk.Entry(frame_insert_poolvisit)
entry_pool_duration.grid(row=1, column=1)

tk.Label(frame_insert_poolvisit, text="Дата посещения (ГГГГ-ММ-ДД):").grid(row=2, column=0)
entry_pool_date = tk.Entry(frame_insert_poolvisit)
entry_pool_date.grid(row=2, column=1)

btn_insert = tk.Button(frame_insert_poolvisit, text="Вставить посещение", command=insert_poolvisit)
btn_insert.grid(row=3, columnspan=2, pady=10)


# Кнопка для чтения данных
btn_fetch = tk.Button(root, text="Проверить активность", command=check_activity)
btn_fetch.pack(pady=5)

# Treeview для отображения данных
frame_table = tk.Frame(root)
frame_table.pack()

columns = ("Дата", "Теги активностей", "Оценка")
tree_movies = ttk.Treeview(frame_table, columns=columns, show="headings")
for i in range(len(columns)):
    if i == 1:
        tree_movies.heading(columns[i], text=columns[i])
        tree_movies.column(columns[i], width=300)
    else:
        tree_movies.heading(columns[i], text=columns[i])
        tree_movies.column(columns[i], width=100)

tree_movies.pack()


root.mainloop()
