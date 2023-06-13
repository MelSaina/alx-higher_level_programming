#include <Python.h>
void print_python_list_info(PyObject *p)
{
	int size, alloc, m;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for ( m = 0; m < size; m++)
	{
		printf("Element %d: ", m);

		obj = PyList_GetItem(p, m);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
