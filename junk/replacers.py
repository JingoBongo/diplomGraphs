
list = '1234.55gdfgdg23,45sdfsdf;'

prop_m_suffix = ''.join([i for i in list if not i.isdigit()])
print(prop_m_suffix)