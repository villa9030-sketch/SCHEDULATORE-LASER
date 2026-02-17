import sqlite3

conn = sqlite3.connect(r'c:\Users\39334\Documents\SCHEDULATORE LASER\app\database\scheduler.db')
cursor = conn.cursor()

# Elimina tutti i record dalle tabelle
cursor.execute('DELETE FROM processing_steps')
cursor.execute('DELETE FROM order_notifications')
cursor.execute('DELETE FROM orders')

conn.commit()
print('✅ Tutti gli ordini, le notifiche e gli step sono stati eliminati dal database')

conn.close()
