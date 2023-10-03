#include <Python.h>
#include <stdio.h>

void print_python_string(PyObject *p) 
{
	if (PyUnicode_Check(p))
	{
		printf("[.] string object info\n");

		if (PyUnicode_IS_COMPACT_ASCII(p)) 
		{
			printf("    type: compact ascii\n");
		}
		else if (PyUnicode_IS_COMPACT(p))
		{
			printf("    type: compact unicode object\n");
		}
		else
		{
			printf("    type: compact string object\n");
		}

		Py_ssize_t length = PyUnicode_GET_LENGTH(p);
		const wchar_t *value = PyUnicode_AsWideCharString(p, NULL);
		printf("    length: %ld\n", length);
		printf("    value: %ls\n", value);
		PyMem_Free(value);
	}
	else
	{
		printf("[.] string object info\n");
		printf("    [ERROR] Invalid String Object\n");
	}
}
