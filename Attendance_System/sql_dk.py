import sqlite3
from Jsoncreating import *

def create_database_table():
    conn = sqlite3.connect('danhgia.db')
    cursor = conn.cursor()

    # Tạo bảng trong cơ sở dữ liệu nếu chưa tồn tại
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            user_id INTEGER,
            vector TEXT
        )
    ''')

    conn.commit()
    conn.close()

def insert_data_to_database(name, user_id, vector):
    conn = sqlite3.connect('danhgia.db')
    cursor = conn.cursor()

    # Thêm dữ liệu vào bảng
    cursor.execute('''
        INSERT INTO data (name, user_id, vector)
        VALUES (?, ?, ?)
    ''', (name, user_id, vector))

    conn.commit()
    conn.close()

def main():
    # Tạo bảng nếu chưa tồn tại
    create_database_table()

    # Đường dẫn đến folder 'data'
    data_folder_path = 'data'

    # Lấy danh sách các tệp JSON trong folder 'data'
    existing_json_files = get_existing_json_files(data_folder_path)

    for user_id, name in enumerate(sorted(os.listdir(data_folder_path))):
        if name not in existing_json_files:
            emb = metadata(os.path.join(data_folder_path, name))
            arr_list = emb.tolist()
            json_string = json.dumps(arr_list)

            # Thêm dữ liệu vào cơ sở dữ liệu
            insert_data_to_database(name, user_id, json_string)

if __name__ == "__main__":
    main()
