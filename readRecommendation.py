from recommend.models import RecommendationResult

default_list = []
RecommendationResult.set_bayes(default_list)
RecommendationResult.set_dt(default_list)
RecommendationResult.set_features(default_list)
RecommendationResult.set_mlp(default_list)
RecommendationResult.name = "kaganbaba"
RecommendationResult.picture = "hellosemih"
RecommendationResult.save()
