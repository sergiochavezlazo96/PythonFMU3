from enum import Enum
from random import randint

import pytest

from pythonfmu.enums import Fmi2Causality, Fmi2Initial, Fmi2Variability
from pythonfmu.variables import Boolean, Integer, Real, ScalarVariable, String


SCALAR_VARIABLE_ATTRIBUTES = ["name", "valueReference", "description", "causality", "variability", "initial"]

def test_ScalarVariable_reference_set_once_only():
    v = ScalarVariable('variable')
    v.value_reference = 22

    with pytest.raises(RuntimeError):
        v.value_reference = 33


@pytest.mark.parametrize("causality", list(Fmi2Causality) + [None, ])
@pytest.mark.parametrize("initial", list(Fmi2Initial) + [None, ])
@pytest.mark.parametrize("variability", list(Fmi2Variability) + [None, ])
@pytest.mark.parametrize("name, description", [
    ("var", None),
    ("var", "description of var"),
])
def test_ScalarVariable_constructor(causality, initial, variability, name, description):
    var = ScalarVariable(name, causality, description, initial, variability)

    assert var.name == name
    assert var.value_reference is None
    assert var.causality == causality
    assert var.description == description
    assert var.initial == initial
    assert var.variability == variability


@pytest.mark.parametrize("causality", list(Fmi2Causality) + [None, ])
@pytest.mark.parametrize("initial", list(Fmi2Initial) + [None, ])
@pytest.mark.parametrize("variability", list(Fmi2Variability) + [None, ])
@pytest.mark.parametrize("name, description", [
    ("var", None),
    ("var", "description of var"),
])
def test_ScalarVariable_to_xml(causality, initial, variability, name, description):
    var = ScalarVariable(name, causality, description, initial, variability)
    valueReference = randint(0, 25000)
    var.value_reference = valueReference

    node = var.to_xml()
    assert node.tag == 'ScalarVariable'
    args = locals()
    for attr in SCALAR_VARIABLE_ATTRIBUTES:
        value = args[attr]
        if value is not None:
            if isinstance(value, Enum):
                assert node.attrib[attr] == value.name
            else:
                assert node.attrib[attr] == str(value)

@pytest.mark.parametrize("name,start", [
    ("boolean_name", None),
    ("boolean_another_name", False),
])
def test_Boolean_constructor(name, start):
    r = Boolean(name, start)

    assert r.start == start

@pytest.mark.parametrize("name,start", [
    ("boolean_name", None),
    ("boolean_another_name", True),
])
def test_Boolean_to_xml(name, start):
    r = Boolean(name, start)
    xml = r.to_xml()
    children = list(xml)
    assert len(children) == 1
    if start is not None:
        assert children[0].attrib['start'] == str(start)

@pytest.mark.parametrize("name,start", [
    ("integer_name", None),
    ("integer_another_name", 42),
])
def test_Integer_constructor(name, start):
    r = Integer(name, start)

    assert r.start == start

@pytest.mark.parametrize("name,start", [
    ("integer_name", None),
    ("integer_another_name", 42),
])
def test_Integer_to_xml(name, start):
    r = Integer(name, start)
    xml = r.to_xml()
    children = list(xml)
    assert len(children) == 1
    if start is not None:
        assert children[0].attrib['start'] == str(start)

@pytest.mark.parametrize("name,start", [
    ("real_name", None),
    ("real_another_name", 22.),
])
def test_Real_constructor(name, start):
    r = Real(name, start)

    assert r.start == start

@pytest.mark.parametrize("name,start", [
    ("real_name", None),
    ("real_another_name", 22.),
])
def test_Real_to_xml(name, start):
    r = Real(name, start)
    xml = r.to_xml()
    children = list(xml)
    assert len(children) == 1
    if start is not None:
        assert children[0].attrib['start'] == str(start)

@pytest.mark.parametrize("name,start", [
    ("string_name", None),
    ("string_another_name", "dummy"),
])
def test_String_constructor(name, start):
    r = String(name, start)

    assert r.start == start

@pytest.mark.parametrize("name,start", [
    ("string_name", None),
    ("string_another_name", "dummy"),
])
def test_String_to_xml(name, start):
    r = String(name, start)
    xml = r.to_xml()
    children = list(xml)
    assert len(children) == 1
    if start is not None:
        assert children[0].attrib['start'] == str(start)