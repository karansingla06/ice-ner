# -*- coding: utf-8 -*-

from .ice_commons.data.dl.manager import ProjectManager

CUSTOM_ENGINES_DIC = {"er.engines.mitie_ner.MitieCustomNER": "ice_commons.er.engines.mitie_ner.MitieCustomNER",
                      "er.engines.corenlp_ner.CorenlpCustomNER": "ice_commons.er.engines.corenlp_ner.CorenlpCustomNER",
                        "er.engines.crf_ner.CRFCustomNER": "ice_commons.er.engines.crf_ner.CRFCustomNER",
                      "er.engines.spacy_ner.SpacyCustomNER": "ice_commons.er.engines.spacy_ner.SpacyCustomNER",
                  "er.engines.spanish.mitie_ner.MitieSpanishCustomNER": "ice_commons.er.engines.spanish.mitie_ner.MitieSpanishCustomNER",
                  "er.engines.spanish.crf_ner.CRFSpanishCustomNER": "ice_commons.er.engines.spanish.crf_ner.CRFSpanishCustomNER",
                  "er.engines.spanish.corenlp_ner.CorenlpSpanishCustomNER": "ice_commons.er.engines.spanish.corenlp_ner.CorenlpSpanishCustomNER"
                  }

DEFAULT_ENGINES_DIC = {"er.engines.mitie_ner.MitieDefaultNER": "ice_commons.er.engines.mitie_ner.MitieDefaultNER",
                   "er.engines.spanish.mitie_ner.MitieSpanishDefaultNER": "ice_commons.er.engines.spanish.mitie_ner.MitieSpanishDefaultNER",
                   "er.engines.corenlp_ner.CorenlpDefaultNER": "ice_commons.er.engines.corenlp_ner.CorenlpDefaultNER",
                   "er.engines.spacy_ner.SpacyDefaultNER": "ice_commons.er.engines.spacy_ner.SpacyDefaultNER",
                   "er.engines.spanish.spacy_ner.SpacySpanishDefaultNER": "ice_commons.er.engines.spanish.spacy_ner.SpacySpanishDefaultNER",
                   "er.engines.spanish.corenlp_ner.CorenlpSpanishDefaultNER": "ice_commons.er.engines.spanish.corenlp_ner.CorenlpSpanishDefaultNER"
                   }



obj = ProjectManager()
all_models = obj.find_all_model()

for model in all_models:
    # print model
    if 'predefined_entity_model' in model and 'custom_entity_model' in model and 'serviceid' in model:
        if str(model['custom_entity_model']) in list(CUSTOM_ENGINES_DIC.keys()) and str(model['predefined_entity_model']) in list(DEFAULT_ENGINES_DIC.keys()):
            obj.update_entity_model_ice_commons(model['serviceid'], DEFAULT_ENGINES_DIC[model['predefined_entity_model']], CUSTOM_ENGINES_DIC[model['custom_entity_model']])