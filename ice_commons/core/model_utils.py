CUSTOM_ENGINES = {"ice_commons.er.engines.mitie_ner.MitieCustomNER": "ICE", "ice_commons.er.engines.corenlp_ner.CorenlpCustomNER": "CoreNLP",
                  "ice_commons.er.engines.crf_ner.CRFCustomNER": "CRF", "ice_commons.er.engines.spacy_ner.SpacyCustomNER": "SPACY",
                  "ice_commons.er.engines.spanish.mitie_ner.MitieSpanishCustomNER": "ICE-es",
                  "ice_commons.er.engines.spanish.crf_ner.CRFSpanishCustomNER": "CRF-es",
                  "ice_commons.er.engines.spanish.corenlp_ner.CorenlpSpanishCustomNER": "CoreNLP-es",
                  }

DEFAULT_ENGINES = {"ice_commons.er.engines.mitie_ner.MitieDefaultNER": "ICE",
                   "ice_commons.er.engines.spanish.mitie_ner.MitieSpanishDefaultNER": "ICE-es",
                   "ice_commons.er.engines.corenlp_ner.CorenlpDefaultNER": "CoreNLP",
                   "ice_commons.er.engines.spacy_ner.SpacyDefaultNER": "SPACY",
                   "ice_commons.er.engines.spanish.spacy_ner.SpacySpanishDefaultNER": "SPACY-es",
                   "ice_commons.er.engines.spanish.corenlp_ner.CorenlpSpanishDefaultNER": "CoreNLP-es"
                   }

DEFAULT_MODELS = {'ice_commons.er.engines.spacy_ner.SpacyDefaultNER': ["PERSON", "NORP", "FAC", "ORG", "GPE", "LOC", "PRODUCT",
                                                           "EVENT", "WORK_OF_ART", "LANGUAGE","ORDINAL"],
                  'ice_commons.er.engines.spanish.spacy_ner.SpacySpanishDefaultNER': ["PER", "LOC", "ORG", "MISC"],
                  'ice_commons.er.engines.mitie_ner.MitieDefaultNER': ["PERSON", "ORGANIZATION", "LOCATION"],
                  'ice_commons.er.engines.spanish.mitie_ner.MitieSpanishDefaultNER': ["PERSON", "ORGANIZATION", "LOCATION"],
                  'ice_commons.er.engines.spanish.corenlp_ner.CorenlpSpanishDefaultNER': ["CAUSE_OF_DEATH", "CITY", "COUNTRY",
                                                                              "CRIMINAL_CHARGE",
                                                                              "EMAIL", "IDEOLOGY", "NATIONALITY",
                                                                              "RELIGION",
                                                                              "STATE_OR_PROVINCE", "TITLE", "URL",
                                                                              "ORDINAL","LOCATION",
                                                                              "DEGREE",
                                                                              "ORGANIZATION", "PERSON","MISC"],
                  'ice_commons.er.engines.corenlp_ner.CorenlpDefaultNER': ["CAUSE_OF_DEATH", "CITY", "COUNTRY", "CRIMINAL_CHARGE",
                                                               "EMAIL", "IDEOLOGY", "NATIONALITY", "RELIGION",
                                                               "STATE_OR_PROVINCE", "TITLE", "URL", "ORDINAL",
                                                            "LOCATION", "DEGREE", "ORGANIZATION", "PERSON", "MISC"]
                  }

DEFAULT_MODELS_CELERY = {'ice_commons.er.engines.spacy_ner.SpacyDefaultNER': ["PERSON", "NORP", "FAC", "ORG", "GPE", "LOC",
                                                                  "PRODUCT", "EVENT", "WORK_OF_ART", "LANGUAGE", "ORDINAL"],
                         'ice_commons.er.engines.spanish.spacy_ner.SpacySpanishDefaultNER': ["PER", "LOC", "ORG", "MISC"]
                         }

CoreNLP_ENGINES = {"CoreNLP": "ice_commons.er.engines.corenlp_ner.CorenlpNER",
                   "CoreNLP-es": "ice_commons.er.engines.spanish.corenlp_ner.CorenlpSpanishNER"}

CoreNLP_DEFAULT_ENGINES = {"CoreNLP": "ice_commons.er.engines.corenlp_ner.CorenlpDefaultNER",
                           "CoreNLP-es": "ice_commons.er.engines.spanish.corenlp_ner.CorenlpSpanishDefaultNER"}

CoreNLP_CUSTOM_ENGINES = {"CoreNLP": "ice_commons.er.engines.corenlp_ner.CorenlpCustomNER",
                          "CoreNLP-es": "ice_commons.er.engines.spanish.corenlp_ner.CorenlpSpanishCustomNER"}


def get_engine(model_class_name):
    if model_class_name in CUSTOM_ENGINES:
        return CUSTOM_ENGINES[model_class_name]
    elif model_class_name in DEFAULT_ENGINES:
        return DEFAULT_ENGINES[model_class_name]
    else:
        raise Exception("Invalid Configuration - No model class")


def get_all_corenlp_engines():
    return list(CoreNLP_ENGINES.keys())


def get_corenlp_default_model(engine):
    return CoreNLP_DEFAULT_ENGINES[engine]


def get_corenlp_custom_model(engine):
    return CoreNLP_CUSTOM_ENGINES[engine]


def get_entities_for_default_model(entity_class):
    if entity_class in DEFAULT_MODELS:
        return DEFAULT_MODELS[entity_class]
    else:
        return []

def get_default_models():
    return list(DEFAULT_MODELS.keys())


def get_default_models_celery():
    return list(DEFAULT_MODELS_CELERY.keys())
