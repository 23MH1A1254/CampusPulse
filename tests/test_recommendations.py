from src.recommendations import build_recommendations

def test_low_scores_generate_tips():
    tips = build_recommendations(30, 40, 45, 6.0, 0, 0, 0, 0)
    assert len(tips) >= 5
    assert any("coding" in tip.lower() for tip in tips)

def test_balanced_profile_has_general_tip():
    tips = build_recommendations(90, 90, 90, 9.0, 4, 2, 4, 3)
    assert len(tips) == 1
    assert "Good profile balance" in tips[0]
