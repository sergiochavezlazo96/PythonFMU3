
#include <Python.h>
#include <iostream>
#include <jni.h>
#include <sstream>

extern "C" {

JNIEXPORT jstring JNICALL Java_no_ntnu_ihb_pythonfmu_Native_getModelDescription(JNIEnv* env, jobject obj, jstring jScriptPath)
{

    Py_Initialize();

    const char* scriptPath = env->GetStringUTFChars(jScriptPath, nullptr);
    std::ostringstream oss;
    oss << "import sys\n";
    oss << "sys.path.append('" << scriptPath << "')\n";

    PyRun_SimpleString(oss.str().c_str());

    env->ReleaseStringUTFChars(jScriptPath, scriptPath);

    PyObject* pModule = PyImport_ImportModule("model");
    PyObject* modelClass = PyObject_GetAttrString(pModule, "Model");
    PyObject* modelInstance = PyObject_CallFunctionObjArgs(modelClass, nullptr);

    PyObject* pFunc;
    pFunc = PyObject_CallMethod(modelInstance, "define", nullptr);
    Py_XDECREF(pFunc);

    PyObject* pyXml = PyObject_GetAttrString(modelInstance, "xml");
    const char* xml = PyUnicode_AsUTF8(pyXml);

    Py_FinalizeEx();


    return env->NewStringUTF(xml);
}

}
