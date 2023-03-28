from docxtpl import DocxTemplate

doc = DocxTemplate("tpl.docx")


def create_training_sheet(class_name: str, subject_name: str, tpl_name: str, *args: list) -> None:
    doc = DocxTemplate(tpl_name)
    data = sorted(args, key=lambda x:x[0])
    cnt = 1
    context = {
        'class_name': class_name,
        'subject_name': subject_name,
        'marks': []
    }
    for el in data:
        context['marks'].append(
                {
                    'num': cnt,
                    'fio': el[0],
                    'mark': el[1]
                }
            )
        cnt += 1

    doc.render(context)
    doc.save("res.docx")

create_training_sheet("3И", "Математика", "tpl.docx",  
                      ("Петров Петр", "5"),  
                      ("Иванов Иван", "5"),  
                      ("Сергеев Сергей", "3"),  
                      ("Никитин Никита", "4"))