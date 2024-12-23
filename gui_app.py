import tkinter as tk
from tkinter import messagebox, ttk, Toplevel
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

def delete_database():
    try:
        conn = create_connection()
        conn.autocommit = True
        cur = conn.cursor()

        database_name = "activities2"

        cur.execute(f"DROP DATABASE {database_name};")
        messagebox.showinfo("Успех", f"База данных '{database_name}' удалена")

        cur.close()
        conn.close()

    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось удалить базу данных: {e}")

def open_insert_movie_window():
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

    window = Toplevel(root)
    window.title("Вставить фильм")
    window.geometry("300x200")

    tk.Label(window, text="Название:").grid(row=0, column=0)
    entry_movie_title = tk.Entry(window)
    entry_movie_title.grid(row=0, column=1)

    tk.Label(window, text="Жанр:").grid(row=1, column=0)
    entry_movie_genre = tk.Entry(window)
    entry_movie_genre.grid(row=1, column=1)

    tk.Label(window, text="Дата просмотра (ГГГГ-ММ-ДД):").grid(row=2, column=0)
    entry_movie_date = tk.Entry(window)
    entry_movie_date.grid(row=2, column=1)

    btn_insert = tk.Button(window, text="Вставить", command=insert_movie)
    btn_insert.grid(row=3, columnspan=2, pady=10)

def open_insert_walk_window():
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

    window = Toplevel(root)
    window.title("Вставить прогулку")
    window.geometry("300x200")

    tk.Label(window, text="Имя друга:").grid(row=0, column=0)
    entry_walk_friend_name = tk.Entry(window)
    entry_walk_friend_name.grid(row=0, column=1)

    tk.Label(window, text="Длительность:").grid(row=1, column=0)
    entry_walk_duration = tk.Entry(window)
    entry_walk_duration.grid(row=1, column=1)

    tk.Label(window, text="Дата прогулки (ГГГГ-ММ-ДД):").grid(row=2, column=0)
    entry_walk_date = tk.Entry(window)
    entry_walk_date.grid(row=2, column=1)

    btn_insert = tk.Button(window, text="Вставить", command=insert_walk)
    btn_insert.grid(row=3, columnspan=2, pady=10)

def open_insert_poolvisit_window():
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

    window = Toplevel(root)
    window.title("Вставить посещение бассейна")
    window.geometry("300x200")

    tk.Label(window, text="Название клуба:").grid(row=0, column=0)
    entry_pool_name = tk.Entry(window)
    entry_pool_name.grid(row=0, column=1)

    tk.Label(window, text="Длительность:").grid(row=1, column=0)
    entry_pool_duration = tk.Entry(window)
    entry_pool_duration.grid(row=1, column=1)

    tk.Label(window, text="Дата посещения (ГГГГ-ММ-ДД):").grid(row=2, column=0)
    entry_pool_date = tk.Entry(window)
    entry_pool_date.grid(row=2, column=1)

    btn_insert = tk.Button(window, text="Вставить", command=insert_poolvisit)
    btn_insert.grid(row=3, columnspan=2, pady=10)

def open_delete_movie_window():
    def delete_movie():
        movie_title = entry_movie_title.get()
        movie_date = entry_movie_date.get()

        conn = create_connection()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute(
                    "SELECT delete_movie_by_title_and_date(%s, %s)",
                    (movie_title, movie_date)
                )
                conn.commit()
                messagebox.showinfo("Успех", "Фильм успешно удален")
            except Exception as e:
                messagebox.showerror("Ошибка", str(e))
            finally:
                cur.close()
                conn.close()

    window = Toplevel(root)
    window.title("Удалить фильм")
    window.geometry("300x200")

    tk.Label(window, text="Название фильма:").grid(row=0, column=0)
    entry_movie_title = tk.Entry(window)
    entry_movie_title.grid(row=0, column=1)

    tk.Label(window, text="Дата (ГГГГ-ММ-ДД):").grid(row=1, column=0)
    entry_movie_date = tk.Entry(window)
    entry_movie_date.grid(row=1, column=1)

    btn_delete = tk.Button(window, text="Удалить", command=delete_movie)
    btn_delete.grid(row=2, columnspan=2, pady=10)

def open_delete_poolvisit_window():
    def delete_poolvisit():
        club_name = entry_club_name.get()
        visit_date = entry_visit_date.get()

        conn = create_connection()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute(
                    "SELECT delete_poolvisit_by_name_and_date(%s, %s)",
                    (club_name, visit_date)
                )
                conn.commit()
                messagebox.showinfo("Успех", "Посещение успешно удалено")
            except Exception as e:
                messagebox.showerror("Ошибка", str(e))
            finally:
                cur.close()
                conn.close()

    window = Toplevel(root)
    window.title("Удалить посещение бассейна")
    window.geometry("300x200")

    tk.Label(window, text="Название клуба:").grid(row=0, column=0)
    entry_club_name = tk.Entry(window)
    entry_club_name.grid(row=0, column=1)

    tk.Label(window, text="Дата (ГГГГ-ММ-ДД):").grid(row=1, column=0)
    entry_visit_date = tk.Entry(window)
    entry_visit_date.grid(row=1, column=1)

    btn_delete = tk.Button(window, text="Удалить", command=delete_poolvisit)
    btn_delete.grid(row=2, columnspan=2, pady=10)

def open_delete_walk_window():
    def delete_walk():
        friend_name = entry_friend_name.get()
        walk_date = entry_walk_date.get()

        conn = create_connection()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute(
                    "SELECT delete_walk_by_name_and_date(%s, %s)",
                    (friend_name, walk_date)
                )
                conn.commit()
                messagebox.showinfo("Успех", "Прогулка успешно удалена")
            except Exception as e:
                messagebox.showerror("Ошибка", str(e))
            finally:
                cur.close()
                conn.close()

    window = Toplevel(root)
    window.title("Удалить прогулку")
    window.geometry("300x200")

    tk.Label(window, text="Имя друга:").grid(row=0, column=0)
    entry_friend_name = tk.Entry(window)
    entry_friend_name.grid(row=0, column=1)

    tk.Label(window, text="Дата (ГГГГ-ММ-ДД):").grid(row=1, column=0)
    entry_walk_date = tk.Entry(window)
    entry_walk_date.grid(row=1, column=1)

    btn_delete = tk.Button(window, text="Удалить", command=delete_walk)
    btn_delete.grid(row=2, columnspan=2, pady=10)


def check_activity():
    conn = create_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM get_all_dailyactivities()")
            rows = cur.fetchall()

            for i in tree_movies.get_children():
                tree_movies.delete(i)

            for row in rows:
                tree_movies.insert("", tk.END, values=row)

        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
        finally:
            cur.close()
            conn.close()

def delete_movies():
    conn = create_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute(
                "DELETE FROM Movies"
            )
            conn.commit()
            messagebox.showinfo("Успех", "Данные о фильмах удалены")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
        finally:
            cur.close()
            conn.close()

def delete_walks():
    conn = create_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute(
                "DELETE FROM Walks"
            )
            conn.commit()
            messagebox.showinfo("Успех", "Данные о прогулках удалены")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
        finally:
            cur.close()
            conn.close()

def delete_poolvisits():
    conn = create_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute(
                "DELETE FROM Movies"
            )
            conn.commit()
            messagebox.showinfo("Успех", "Данные о посещениях бассейна удалены")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
        finally:
            cur.close()
            conn.close()

def delete_dailyactivities():
    conn = create_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute(
                "DELETE FROM DailyActivities"
            )
            conn.commit()
            messagebox.showinfo("Успех", "Данные учета активности удалены")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
        finally:
            cur.close()
            conn.close()

def delete_all():
    conn = create_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute(
                "DELETE FROM Movies"
            )
            cur.execute(
                "DELETE FROM Walks"
            )
            cur.execute(
                "DELETE FROM PoolVisits"
            )
            cur.execute(
                "DELETE FROM DailyActivities"
            )
            conn.commit()
            messagebox.showinfo("Успех", "Таблицы очищены")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
        finally:
            cur.close()
            conn.close()

def open_search_movies_window():
    def search_movie():
        movie_title = entry_movie_title.get()
        
        conn = create_connection()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute(
                    "SELECT * FROM movies WHERE title = %s",
                    (movie_title,)
                )
                rows = cur.fetchall()

                for i in tree_results.get_children():
                    tree_results.delete(i)

                for row in rows:
                    tree_results.insert("", tk.END, values=row)

            except Exception as e:
                messagebox.showerror("Ошибка", str(e))
            finally:
                cur.close()
                conn.close()

    window = Toplevel(root)
    window.title("Поиск фильма")
    window.geometry("500x400")

    tk.Label(window, text="Название фильма:").pack(pady=10)
    entry_movie_title = tk.Entry(window, width=30)
    entry_movie_title.pack(pady=5)

    btn_search = tk.Button(window, text="Искать", command=search_movie)
    btn_search.pack(pady=10)

    frame_results = tk.Frame(window)
    frame_results.pack(pady=10)

    columns = ("ID", "Название", "Жанр", "Дата просмотра")
    tree_results = ttk.Treeview(frame_results, columns=columns, show="headings")
    for col in columns:
        tree_results.heading(col, text=col)
        tree_results.column(col, width=120)

    tree_results.pack()

def open_search_walks_window():
    def search_walks():
        friend_name = entry_friend_name.get()
        
        conn = create_connection()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute(
                    "SELECT * FROM walks WHERE friend_name = %s",
                    (friend_name,)
                )
                rows = cur.fetchall()

                for i in tree_results.get_children():
                    tree_results.delete(i)

                for row in rows:
                    tree_results.insert("", tk.END, values=row)

            except Exception as e:
                messagebox.showerror("Ошибка", str(e))
            finally:
                cur.close()
                conn.close()

    window = Toplevel(root)
    window.title("Поиск прогулки")
    window.geometry("500x400")

    tk.Label(window, text="Имя друга:").pack(pady=10)
    entry_friend_name = tk.Entry(window, width=30)
    entry_friend_name.pack(pady=5)

    btn_search = tk.Button(window, text="Искать", command=search_walks)
    btn_search.pack(pady=10)

    frame_results = tk.Frame(window)
    frame_results.pack(pady=10)

    columns = ("ID", "Имя друга", "Длительность", "Дата прогулки")
    tree_results = ttk.Treeview(frame_results, columns=columns, show="headings")
    for col in columns:
        tree_results.heading(col, text=col)
        tree_results.column(col, width=120)

    tree_results.pack()

def open_search_poolvisits_window():
    def search_poolvisits():
        club_name = entry_club_name.get()
        
        conn = create_connection()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute(
                    "SELECT * FROM poolvisits WHERE club_name = %s",
                    (club_name,)
                )
                rows = cur.fetchall()

                for i in tree_results.get_children():
                    tree_results.delete(i)

                for row in rows:
                    tree_results.insert("", tk.END, values=row)

            except Exception as e:
                messagebox.showerror("Ошибка", str(e))
            finally:
                cur.close()
                conn.close()

    window = Toplevel(root)
    window.title("Поиск посещений бассейна")
    window.geometry("500x400")

    tk.Label(window, text="Название клуба:").pack(pady=10)
    entry_club_name = tk.Entry(window, width=30)
    entry_club_name.pack(pady=5)

    btn_search = tk.Button(window, text="Искать", command=search_poolvisits)
    btn_search.pack(pady=10)

    frame_results = tk.Frame(window)
    frame_results.pack(pady=10)

    columns = ("ID", "Название клуба", "Длительность", "Дата посещения")
    tree_results = ttk.Treeview(frame_results, columns=columns, show="headings")
    for col in columns:
        tree_results.heading(col, text=col)
        tree_results.column(col, width=120)

    tree_results.pack()

root = tk.Tk()
root.title("Учет активности студентов")
root.geometry("700x800")

btn_delete_db = tk.Button(root, text="Delete Database", command=delete_database)
btn_delete_db.place(x=600, y=10)

btn_open_movie_form = tk.Button(root, text="Добавить фильм", command=open_insert_movie_window)
btn_open_movie_form.pack(pady=5)

btn_open_walk_form = tk.Button(root, text="Добавить прогулку", command=open_insert_walk_window)
btn_open_walk_form.pack(pady=5)

btn_open_poolvisit_form = tk.Button(root, text="Добавить посещение бассейна", command=open_insert_poolvisit_window)
btn_open_poolvisit_form.pack(pady=5)

btn_open_delete_movie_form = tk.Button(root, text="Удалить фильм", command=open_delete_movie_window)
btn_open_delete_movie_form.pack(pady=5)

btn_open_delete_walk_form = tk.Button(root, text="Удалить прогулку", command=open_delete_walk_window)
btn_open_delete_walk_form.pack(pady=5)

btn_open_delete_poolvisit_form = tk.Button(root, text="Удалить посещение бассейна", command=open_delete_poolvisit_window)
btn_open_delete_poolvisit_form.pack(pady=5)

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

btn_fetch = tk.Button(root, text="Проверить активность", command=check_activity)
btn_fetch.pack(pady=5)

btn_open_delete_movies_form = tk.Button(root, text="Очистить таблицу с фильмами", command=delete_movies)
btn_open_delete_movies_form.pack(pady=5)

btn_open_delete_walks_form = tk.Button(root, text="Очистить таблицу с прогулками", command=delete_walks)
btn_open_delete_walks_form.pack(pady=5)

btn_open_delete_poolvisits_form = tk.Button(root, text="Очистить таблицу с посещениями бассейнов", command=delete_poolvisits)
btn_open_delete_poolvisits_form.pack(pady=5)

btn_open_delete_dailyactivities_form = tk.Button(root, text="Очистить таблицу учета активности", command=delete_dailyactivities)
btn_open_delete_dailyactivities_form.pack(pady=5)

btn_open_delete_all_form = tk.Button(root, text="Очистить все таблицы", command=delete_all)
btn_open_delete_all_form.pack(pady=5)

btn_open_search_movie_form = tk.Button(root, text="Поиск фильмов", command=open_search_movies_window)
btn_open_search_movie_form.pack(pady=5)

btn_open_search_movie_form = tk.Button(root, text="Поиск прогулок", command=open_search_walks_window)
btn_open_search_movie_form.pack(pady=5)

btn_open_search_movie_form = tk.Button(root, text="Поиск посещения бассейна", command=open_search_poolvisits_window)
btn_open_search_movie_form.pack(pady=5)

root.mainloop()
