# ---------  String ------------
# Old
print('%s %s' % ('one', 'two'))

# New
print('{} {}'.format('one', 'two'))

# --------- Number --------------
# Old
print('%d %d' % (1, 2))

# New
print('{} {}'.format(1, 2))

# New, sắp xếp lại thứ tự argument khi tạo string
print('{1} {0}'.format('one', 'two'))

