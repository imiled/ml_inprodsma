"""Test for the model."""
from trainer import model

def test_build_model():
    """Test the build_model function."""
    m= model.build_model()
    assert m.layers is not None
    assert m.layers !=[]
