count=0
Sample_data = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
for i in Sample_data:
    if i.get('success')==True:
        count+=1
print(count)