"""
Лаб9
Вариант 4 -колво шагов с суммой
(поля ввода: steps,date)
Афрузунова Дарья 502744
"""

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask('Steps tracker')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db = SQLAlchemy(app)


class StepsRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    steps = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'StepsRecord{self.id}. {self.date} - {self.steps} шагов'


@app.route('/')
def main():
    records = StepsRecord.query.all()
    total_steps = sum(record.steps for record in records)
    return render_template('index.html', records=records, total_steps=total_steps)


@app.route('/add', methods=['POST'])
def add_record():
    data = request.json
    record = StepsRecord(steps=data['steps'], date=data['date'])
    db.session.add(record)
    db.session.commit()
    return 'OK'


@app.route('/clear', methods=['POST'])
def clear_records():
    StepsRecord.query.delete()
    db.session.commit()
    return 'OK'


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
