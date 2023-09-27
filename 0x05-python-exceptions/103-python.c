/*
 * File: 103-python.c
 * Auth: mariam
 */

#include <Python.h>

void print_python_list_info(PyObject *p);
void print_python_bytes_info(PyObject *p);
void print_python_float_info(PyObject *p);

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, alloc, i;
	const char *elem_type;
	PyListObject *list_obj = (PyListObject *)p;
	PyVarObject *var_obj = (PyVarObject *)p;

	size = var_obj->ob_size;
	alloc = list_obj->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (i = 0; i < size; i++)
	{
		elem_type = list_obj->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, elem_type);
		if (strcmp(elem_type, "bytes") == 0)
			print_python_bytes_info(list_obj->ob_item[i]);
		else if (strcmp(elem_type, "float") == 0)
			print_python_float_info(list_obj->ob_item[i]);
	}
}

/**
 * print_python_bytes_info - Prints basic info about Python bytes objects.
 * @p: A PyObject bytes object.
 */
void print_python_bytes_info(PyObject *p)
{
	Py_ssize_t size, i;
	PyBytesObject *bytes_obj = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", bytes_obj->ob_sval);

	if (size >= 10)
		size = 10;
	else
		size++;

	printf("  first %ld bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02hhx", bytes_obj->ob_sval[i]);
		if (i == size - 1)
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float_info - Prints basic info about Python float objects.
 * @p: A PyObject float object.
 */
void print_python_float_info(PyObject *p)
{
	char *buffer = NULL;

	PyFloatObject *float_obj = (PyFloatObject *)p;

	fflush(stdout);

	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	buffer = PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
		Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", buffer);
	PyMem_Free(buffer);
}
