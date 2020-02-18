
#####################################################################################################################
Create new project:

Query:
const saveProjectQuery = `
  mutation AddProject($input: addProjectInput!) {
    addProject(input: $input) {
      changedProjectEdge {
        node {
          id
          _id
          serviceid
          name
          desc,
          custom_entity_model
          predefined_entity_model
          importProject
          visibility
          createdAt
          updatedAt
          createdBy {
            username
          }
          lastAccessed
        }
      }
    }
  }
`;

Request URL:
http://ice-xd.southindia.cloudapp.azure.com:3001/project/manage

POST data:

{
    "input": {
        "createdBy": "58b79a695c280914dc30554b",
        "lastAccessed": "2019-06-26T11: 48: 36.832Z",
        "clientMutationId": "random",
        "masterBot": false,
        "predefined_entity_model": "ice_commons.er.engines.spacy_ner.SpacyDefaultNER",
        "name": "qwerty",
        "desc": "qwerty",
        "visibility": "private",
        "importProject": [],
        "language": "EN",
        "custom_entity_model": "ice_commons.er.engines.crf_ner.CRFCustomNER",
        "nerType": false
    }
}


JSON Response:
{
    "data": {
        "addProject": {
            "changedProjectEdge": {
                "node": {
                    "id": "UHJvamVjdDo1ZDEzNWI4NzE0NGIzNTE0MDMyYjI3Zjk=",
                    "_id": "5d135b87144b3514032b27f9",
                    "serviceid": null,
                    "name": "qwerty",
                    "desc": "qwerty",
                    "custom_entity_model": "ice_commons.er.engines.crf_ner.CRFCustomNER",
                    "predefined_entity_model": "ice_commons.er.engines.spacy_ner.SpacyDefaultNER",
                    "importProject": [],
                    "visibility": "private",
                    "createdAt": "2019-06-26T11:48:23.425Z",
                    "updatedAt": "2019-06-26T11:48:23.425Z",
                    "createdBy": {
                        "username": "visualice"
                    },
                    "lastAccessed": "2019-06-26T11:48:36.832Z"
                }
            }
        }
    }
}

#####################################################################################################################
Update Project:

Query:
const updateProjectQuery = `
    mutation UpdateProject($input: updateProjectInput!) {
     updateProject(input: $input) {
       changedProject{
         id
         _id
         name
         predefined_entity_model
         custom_entity_model
         ner{
           status,
           status_message
         }
         ir{
           status,
           status_message
         }
         serviceid

       }
     }
   }
  `;


Request URL:
http://ice-xd.southindia.cloudapp.azure.com:3001/project/configure/5d135b87144b3514032b27f9
5d135b87144b3514032b27f9 is the project id

POST Data:

{
    "input": {
        "clientMutationId": "random",
        "id": "UHJvamVjdDo1ZDEzNWI4NzE0NGIzNTE0MDMyYjI3Zjk=",
        "desc": "qwerty111"
    },
    "projectId": "5d135b87144b3514032b27f9",
    "userId": "58b79a695c280914dc30554b"
}

JSON Response:

{
    "data": {
        "updateProject": {
            "changedProject": {
                "id": "UHJvamVjdDo1ZDEzNWI4NzE0NGIzNTE0MDMyYjI3Zjk=",
                "_id": "5d135b87144b3514032b27f9",
                "name": "qwerty",
                "predefined_entity_model": "ice_commons.er.engines.spacy_ner.SpacyDefaultNER",
                "custom_entity_model": "ice_commons.er.engines.crf_ner.CRFCustomNER",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "serviceid": "0Ap9STSZbF74ImIbVvtFb4DoJwRB6ABwVswuq5BrZ5TMK7oj9Ti8kGaHre0XD0ND"
            }
        }
    }
}

#####################################################################################################################

Get Project with ID:

Query:

const loadProjectConfigByIdQuery = ` query GetProjectConfig($id: ID!){
    projectconfigs(project: $id){
      id
      _id
      serviceid
      project {
        id
        _id
        name
        desc
        nerType
        masterBot
        importProject
        serviceid
        language
        predefined_entity_model
        custom_entity_model
        visibility
        ner{
          status
          status_message
        }
        ir{
          status
          status_message
        }
         createdBy {
       username
     }
      }
      datasource{
        utterances{
          utterance
          case_converted_utterance
          mapping
          ir_trained
          ner_trained
        }
        id
        serviceid
        entities
        intents{
          name
          description
          createdAt
          modifiedAt
        }
        trainIntent
        trainEntity
        predefined_entities
        patterns{
          pattern
          entity
        }
        phrases{
          phrase
          entity
        }
        synonyms{
          synonym
          word
        }
        }
      integration_markdown
      build_report {
       ner{
         accuracy
       }
       cat{
        report{
          recall
           support
           label
           precision
           f1
       }
       f1_scores
       scores
       confusion_matrix{
         labels
         matrix {
           matrix
           label
         }
       }
     }

     }
    }
  }

  `;

Request URL:
http://ice-xd.southindia.cloudapp.azure.com:3001/project/configure/5d0752ee308aae6a119ae425
5d0752ee308aae6a119ae425 is the project id

POST Data:

{"id":"5d0752ee308aae6a119ae425","createdBy":"58b79a695c280914dc30554b"}

JSON Response:

  {
    "data": {
        "projectconfigs": [
            {
                "id": "UHJvamVjdENvbmZpZzo1ZDA3NTJlZTMwOGFhZTZhMTE5YWU0MjY=",
                "_id": "5d0752ee308aae6a119ae426",
                "serviceid": "0AoI5SB5ILHozOHzl8f5wS5skmejKfp9GcTVayQiYFsCldHPJA1qD4RleUBJfga5",
                "project": {
                    "id": "UHJvamVjdDo1ZDA3NTJlZTMwOGFhZTZhMTE5YWU0MjU=",
                    "_id": "5d0752ee308aae6a119ae425",
                    "name": "devtesting1",
                    "desc": "dev testing1",
                    "nerType": true,
                    "masterBot": false,
                    "importProject": [
                        "5cfe40a4308aae6a118c0ffd"
                    ],
                    "serviceid": "0AoI5SB5ILHozOHzl8f5wS5skmejKfp9GcTVayQiYFsCldHPJA1qD4RleUBJfga5",
                    "language": "EN",
                    "predefined_entity_model": "ice_commons.er.engines.spacy_ner.SpacyDefaultNER",
                    "custom_entity_model": "ice_commons.er.engines.crf_ner.CRFCustomNER",
                    "visibility": "private",
                    "ner": {
                        "status": "new",
                        "status_message": "Some checks haven't completed yet"
                    },
                    "ir": {
                        "status": "new",
                        "status_message": "Some checks haven't completed yet"
                    },
                    "createdBy": {
                        "username": "visualice"
                    }
                },
                "datasource": {
                    "utterances": [
                        {
                            "utterance": "heyyy",
                            "case_converted_utterance": "Heyyy",
                            "mapping": "{\"tokens\":[\"Heyyy\"],\"tags\":[{\"start\":0,\"tag\":\"sample\",\"end\":1,\"entity\":\"heyyy\"}],\"intent\":\"test1\"}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "I want to do a travel",
                            "case_converted_utterance": "I want to do a travel",
                            "mapping": "{\"tokens\": [\"I\", \"want\", \"to\", \"do\", \"a\", \"travel\"], \"intent\": \"travelbooking\", \"tags\": [{\"start\": 5, \"tag\": \"TYPE\", \"end\": 6, \"score\": 0.5640399006298088, \"entity\": \"travel\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "travel booking",
                            "case_converted_utterance": "Travel booking",
                            "mapping": "{\"tokens\": [\"Travel\", \"booking\"], \"intent\": \"travelbooking\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.5286114190311912, \"entity\": \"travel\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "travel",
                            "case_converted_utterance": "Travel",
                            "mapping": "{\"tokens\": [\"Travel\"], \"intent\": \"travelbooking\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.2537922087668458, \"entity\": \"travel\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Please to a flight booking",
                            "case_converted_utterance": "Please to a flight booking",
                            "mapping": "{\"tokens\": [\"Please\", \"to\", \"a\", \"flight\", \"booking\"], \"intent\": \"airlinesearch\", \"tags\": [{\"start\": 3, \"tag\": \"mode\", \"end\": 4, \"entity\": \"flight\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "I would like to travel by flight",
                            "case_converted_utterance": "I would like to travel by flight",
                            "mapping": "{\"tokens\": [\"I\", \"would\", \"like\", \"to\", \"travel\", \"by\", \"flight\"], \"intent\": \"airlinesearch\", \"tags\": [{\"start\": 4, \"tag\": \"TYPE\", \"end\": 5, \"score\": 0.4979866350219423, \"entity\": \"travel\"}, {\"start\": 6, \"tag\": \"mode\", \"end\": 7, \"entity\": \"flight\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "kindly book one flight",
                            "case_converted_utterance": "Kindly book one flight",
                            "mapping": "{\"tokens\": [\"Kindly\", \"book\", \"one\", \"flight\"], \"intent\": \"airlinesearch\", \"tags\": [{\"start\": 3, \"tag\": \"mode\", \"end\": 4, \"entity\": \"flight\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "flight",
                            "case_converted_utterance": "Flight",
                            "mapping": "{\"tokens\": [\"Flight\"], \"intent\": \"airlinesearch\", \"tags\": [{\"start\": 0, \"tag\": \"mode\", \"end\": 1, \"entity\": \"flight\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Please book a flight ticket for me",
                            "case_converted_utterance": "Please book a flight ticket for me",
                            "mapping": "{\"tokens\": [\"Please\", \"book\", \"a\", \"flight\", \"ticket\", \"for\", \"me\"], \"intent\": \"airlinesearch\", \"tags\": [{\"start\": 0, \"tag\": \"mode\", \"end\": 1, \"entity\": \"\"}, {\"start\": 3, \"tag\": \"mode\", \"end\": 4, \"entity\": \"flight\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Please do a travel booking",
                            "case_converted_utterance": "Please do a travel booking",
                            "mapping": "{\"tokens\": [\"Please\", \"do\", \"a\", \"travel\", \"booking\"], \"intent\": \"travelbooking\", \"tags\": [{\"start\": 3, \"tag\": \"TYPE\", \"end\": 4, \"score\": 0.6740128800829303, \"entity\": \"travel\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "I want to travel",
                            "case_converted_utterance": "I want to travel",
                            "mapping": "{\"tokens\": [\"I\", \"want\", \"to\", \"travel\"], \"intent\": \"travelbooking\", \"tags\": [{\"start\": 3, \"tag\": \"TYPE\", \"end\": 4, \"score\": 0.3422346315669714, \"entity\": \"travel\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "I want travel",
                            "case_converted_utterance": "I want travel",
                            "mapping": "{\"tokens\": [\"I\", \"want\", \"travel\"], \"intent\": \"travelbooking\", \"tags\": [{\"start\": 2, \"tag\": \"TYPE\", \"end\": 3, \"score\": 0.23075157859533177, \"entity\": \"travel\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "I want to do booking",
                            "case_converted_utterance": "I want to do booking",
                            "mapping": "{\"tokens\": [\"I\", \"want\", \"to\", \"do\", \"booking\"], \"intent\": \"booking\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Please do a booking",
                            "case_converted_utterance": "Please do a booking",
                            "mapping": "{\"tokens\": [\"Please\", \"do\", \"a\", \"booking\"], \"intent\": \"booking\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Please booking",
                            "case_converted_utterance": "Please booking",
                            "mapping": "{\"tokens\": [\"Please\", \"booking\"], \"intent\": \"booking\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "I want to do a booking",
                            "case_converted_utterance": "I want to do a booking",
                            "mapping": "{\"tokens\": [\"I\", \"want\", \"to\", \"do\", \"a\", \"booking\"], \"intent\": \"booking\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "hiiii",
                            "case_converted_utterance": "Hiiii",
                            "mapping": "{\"tokens\": [\"Hiiii\"], \"intent\": \"Greeting\", \"tags\": [{\"start\": 0, \"tag\": \"MODE\", \"end\": 1, \"score\": 0.1243794318755859, \"entity\": \"hiiii\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "hi",
                            "case_converted_utterance": "Hi",
                            "mapping": "{\"tokens\": [\"Hi\"], \"intent\": \"Greeting\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "heyya",
                            "case_converted_utterance": "Heyya",
                            "mapping": "{\"tokens\": [\"Heyya\"], \"intent\": \"Greeting\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "hello",
                            "case_converted_utterance": "Hello",
                            "mapping": "{\"tokens\": [\"Hello\"], \"intent\": \"Greeting\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "hi",
                            "case_converted_utterance": "Hi",
                            "mapping": "{\"tokens\": [\"Hi\"], \"intent\": \"Greeting\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "You there",
                            "case_converted_utterance": "You there",
                            "mapping": "{\"tokens\": [\"You\", \"there\"], \"intent\": \"Greeting\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Hey",
                            "case_converted_utterance": "Hey",
                            "mapping": "{\"tokens\": [\"Hey\"], \"intent\": \"Greeting\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Hai",
                            "case_converted_utterance": "Hai",
                            "mapping": "{\"tokens\": [\"Hai\"], \"intent\": \"Greeting\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Hi",
                            "case_converted_utterance": "Hi",
                            "mapping": "{\"tokens\": [\"Hi\"], \"intent\": \"Greeting\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Good morning",
                            "case_converted_utterance": "Good morning",
                            "mapping": "{\"tokens\": [\"Good\", \"morning\"], \"intent\": \"Greeting\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.2530555062914658, \"entity\": \"Good\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Good day",
                            "case_converted_utterance": "Good day",
                            "mapping": "{\"tokens\": [\"Good\", \"day\"], \"intent\": \"Greeting\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.2684357011642687, \"entity\": \"Good\"}, {\"start\": 1, \"tag\": \"airport\", \"end\": 2, \"entity\": \"day\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Good evening",
                            "case_converted_utterance": "Good evening",
                            "mapping": "{\"tokens\": [\"Good\", \"evening\"], \"intent\": \"Greeting\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Hey twin",
                            "case_converted_utterance": "Hey twin",
                            "mapping": "{\"tokens\": [\"Hey\", \"twin\"], \"intent\": \"Greeting\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Hi there",
                            "case_converted_utterance": "Hi there",
                            "mapping": "{\"tokens\": [\"Hi\", \"there\"], \"intent\": \"Greeting\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "What'S up ?",
                            "case_converted_utterance": "What'S up ?",
                            "mapping": "{\"tokens\": [\"What'S\", \"up\", \"?\"], \"intent\": \"Greeting\", \"tags\": [{\"start\": 2, \"tag\": \"MODE\", \"end\": 3, \"score\": 0.3594824179203809, \"entity\": \"?\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Who is this ?",
                            "case_converted_utterance": "Who is this ?",
                            "mapping": "{\"tokens\": [\"Who\", \"is\", \"this\", \"?\"], \"intent\": \"Greeting\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "What'S new ?",
                            "case_converted_utterance": "What'S new ?",
                            "mapping": "{\"tokens\": [\"What'S\", \"new\", \"?\"], \"intent\": \"Greeting\", \"tags\": [{\"start\": 0, \"tag\": \"MODE\", \"end\": 1, \"score\": 0.276929868992718, \"entity\": \"What'S\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Hey there",
                            "case_converted_utterance": "Hey there",
                            "mapping": "{\"tokens\": [\"Hey\", \"there\"], \"intent\": \"Greeting\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Ok take me back",
                            "case_converted_utterance": "Ok take me back",
                            "mapping": "{\"tokens\": [\"Ok\", \"take\", \"me\", \"back\"], \"intent\": \"Greeting\", \"tags\": [{\"start\": 2, \"tag\": \"airport\", \"end\": 3, \"entity\": \"me\"}, {\"start\": 3, \"tag\": \"MODE\", \"end\": 4, \"score\": 0.28095878767074006, \"entity\": \"back\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Looking good eve",
                            "case_converted_utterance": "Looking good eve",
                            "mapping": "{\"tokens\": [\"Looking\", \"good\", \"eve\"], \"intent\": \"Greeting\", \"tags\": [{\"start\": 2, \"tag\": \"MODE\", \"end\": 3, \"score\": 0.3454258060185423, \"entity\": \"eve\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "How R U ?",
                            "case_converted_utterance": "How R U ?",
                            "mapping": "{\"tokens\": [\"How\", \"R\", \"U\", \"?\"], \"intent\": \"Greeting\", \"tags\": [{\"start\": 0, \"tag\": \"sample\", \"end\": 4, \"entity\": \"How R U ?\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "How is it going ?",
                            "case_converted_utterance": "How is it going ?",
                            "mapping": "{\"tokens\": [\"How\", \"is\", \"it\", \"going\", \"?\"], \"intent\": \"Greeting\", \"tags\": [{\"start\": 4, \"tag\": \"MODE\", \"end\": 5, \"score\": 0.22077778757291347, \"entity\": \"?\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "How have you been ?",
                            "case_converted_utterance": "How have you been ?",
                            "mapping": "{\"tokens\": [\"How\", \"have\", \"you\", \"been\", \"?\"], \"intent\": \"Greeting\", \"tags\": [{\"start\": 4, \"tag\": \"MODE\", \"end\": 5, \"score\": 0.21941104933103223, \"entity\": \"?\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "How are you today ?",
                            "case_converted_utterance": "How are you today ?",
                            "mapping": "{\"tokens\": [\"How\", \"are\", \"you\", \"today\", \"?\"], \"intent\": \"Greeting\", \"tags\": [{\"start\": 4, \"tag\": \"MODE\", \"end\": 5, \"score\": 0.22229289284995607, \"entity\": \"?\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "How are things going ?",
                            "case_converted_utterance": "How are things going ?",
                            "mapping": "{\"tokens\": [\"How\", \"are\", \"things\", \"going\", \"?\"], \"intent\": \"Greeting\", \"tags\": [{\"start\": 4, \"tag\": \"MODE\", \"end\": 5, \"score\": 0.22077778757291347, \"entity\": \"?\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Hello I am looking for some help here",
                            "case_converted_utterance": "Hello I am looking for some help here",
                            "mapping": "{\"tokens\": [\"Hello\", \"I\", \"am\", \"looking\", \"for\", \"some\", \"help\", \"here\"], \"intent\": \"Greeting\", \"tags\": [{\"start\": 0, \"tag\": \"sample\", \"end\": 3, \"entity\": \"Hello I am\"}, {\"start\": 6, \"tag\": \"TYPE\", \"end\": 7, \"score\": 0.11152091750581689, \"entity\": \"help\"}, {\"start\": 7, \"tag\": \"MODE\", \"end\": 8, \"score\": 0.21238762326047897, \"entity\": \"here\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Hi advisor",
                            "case_converted_utterance": "Hi advisor",
                            "mapping": "{\"tokens\": [\"Hi\", \"advisor\"], \"intent\": \"Greeting\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Hey you",
                            "case_converted_utterance": "Hey you",
                            "mapping": "{\"tokens\": [\"Hey\", \"you\"], \"intent\": \"Greeting\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Hey there all",
                            "case_converted_utterance": "Hey there all",
                            "mapping": "{\"tokens\": [\"Hey\", \"there\", \"all\"], \"intent\": \"Greeting\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Hey how are you doing",
                            "case_converted_utterance": "Hey how are you doing",
                            "mapping": "{\"tokens\": [\"Hey\", \"how\", \"are\", \"you\", \"doing\"], \"intent\": \"Greeting\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Hello",
                            "case_converted_utterance": "Hello",
                            "mapping": "{\"tokens\": [\"Hello\"], \"intent\": \"Greeting\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Hello agent",
                            "case_converted_utterance": "Hello agent",
                            "mapping": "{\"tokens\": [\"Hello\", \"agent\"], \"intent\": \"Greeting\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Have you been well ?",
                            "case_converted_utterance": "Have you been well ?",
                            "mapping": "{\"tokens\": [\"Have\", \"you\", \"been\", \"well\", \"?\"], \"intent\": \"Greeting\", \"tags\": [{\"start\": 2, \"tag\": \"MODE\", \"end\": 3, \"score\": 0.2390684494907248, \"entity\": \"been\"}, {\"start\": 4, \"tag\": \"MODE\", \"end\": 5, \"score\": 0.2158975453646159, \"entity\": \"?\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Greetings",
                            "case_converted_utterance": "Greetings",
                            "mapping": "{\"tokens\": [\"Greetings\"], \"intent\": \"Greeting\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Good to see you",
                            "case_converted_utterance": "Good to see you",
                            "mapping": "{\"tokens\": [\"Good\", \"to\", \"see\", \"you\"], \"intent\": \"Greeting\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "no",
                            "case_converted_utterance": "No",
                            "mapping": "{\"tokens\": [\"No\"], \"intent\": \"conclusionflow\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "no thank you",
                            "case_converted_utterance": "No thank you",
                            "mapping": "{\"tokens\": [\"No\", \"thank\", \"you\"], \"intent\": \"conclusionflow\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "hello",
                            "case_converted_utterance": "Hello",
                            "mapping": "{\"tokens\": [\"Hello\"], \"intent\": \"test1\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "23394 weather",
                            "case_converted_utterance": "23394 weather",
                            "mapping": "{\"tokens\": [\"23394\", \"weather\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"sample\", \"end\": 2, \"entity\": \"23394 weather\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Weather of 23294",
                            "case_converted_utterance": "Weather of 23294",
                            "mapping": "{\"tokens\": [\"Weather\", \"of\", \"23294\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.1381967649210164, \"entity\": \"Weather\"}, {\"start\": 1, \"tag\": \"sample\", \"end\": 3, \"entity\": \"of 23294\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Temperature of 695024",
                            "case_converted_utterance": "Temperature of 695024",
                            "mapping": "{\"tokens\": [\"Temperature\", \"of\", \"695024\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.11583915744592144, \"entity\": \"Temperature\"}, {\"start\": 1, \"tag\": \"sample\", \"end\": 3, \"entity\": \"of 695024\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Temperature of Manchester",
                            "case_converted_utterance": "Temperature of Manchester",
                            "mapping": "{\"tokens\": [\"Temperature\", \"of\", \"Manchester\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.11583915744592144, \"entity\": \"Temperature\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Weather of La",
                            "case_converted_utterance": "Weather of La",
                            "mapping": "{\"tokens\": [\"Weather\", \"of\", \"La\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.1381967649210164, \"entity\": \"Weather\"}, {\"start\": 2, \"tag\": \"airport\", \"end\": 3, \"entity\": \"La\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Zzzz 0Zz weather",
                            "case_converted_utterance": "Zzzz 0Zz weather",
                            "mapping": "{\"tokens\": [\"Zzzz\", \"0Zz\", \"weather\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"sample\", \"end\": 2, \"entity\": \"Zzzz 0Zz\"}, {\"start\": 2, \"tag\": \"MODE\", \"end\": 3, \"score\": 0.10199896814355316, \"entity\": \"weather\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Weather of XXXX XXX",
                            "case_converted_utterance": "Weather of XXXX XXX",
                            "mapping": "{\"tokens\": [\"Weather\", \"of\", \"XXXX\", \"XXX\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.1381967649210164, \"entity\": \"Weather\"}, {\"start\": 1, \"tag\": \"sample\", \"end\": 4, \"entity\": \"of XXXX XXX\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "99900 weather",
                            "case_converted_utterance": "99900 weather",
                            "mapping": "{\"tokens\": [\"99900\", \"weather\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"sample\", \"end\": 2, \"entity\": \"99900 weather\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Trivandrum weather",
                            "case_converted_utterance": "Trivandrum weather",
                            "mapping": "{\"tokens\": [\"Trivandrum\", \"weather\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.10129349747641157, \"entity\": \"Trivandrum\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Weather of Trivandrum",
                            "case_converted_utterance": "Weather of Trivandrum",
                            "mapping": "{\"tokens\": [\"Weather\", \"of\", \"Trivandrum\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.1381967649210164, \"entity\": \"Weather\"}, {\"start\": 2, \"tag\": \"MODE\", \"end\": 3, \"score\": 0.12936659812427925, \"entity\": \"Trivandrum\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Temperature of Trivandrum",
                            "case_converted_utterance": "Temperature of Trivandrum",
                            "mapping": "{\"tokens\": [\"Temperature\", \"of\", \"Trivandrum\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.11583915744592144, \"entity\": \"Temperature\"}, {\"start\": 2, \"tag\": \"MODE\", \"end\": 3, \"score\": 0.12936659812427925, \"entity\": \"Trivandrum\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Climate of Trivandrum",
                            "case_converted_utterance": "Climate of Trivandrum",
                            "mapping": "{\"tokens\": [\"Climate\", \"of\", \"Trivandrum\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.109057259808529, \"entity\": \"Climate\"}, {\"start\": 2, \"tag\": \"MODE\", \"end\": 3, \"score\": 0.12936659812427925, \"entity\": \"Trivandrum\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Show me weather of Chennai",
                            "case_converted_utterance": "Show me weather of Chennai",
                            "mapping": "{\"tokens\": [\"Show\", \"me\", \"weather\", \"of\", \"Chennai\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"MODE\", \"end\": 1, \"score\": 0.14623363065090153, \"entity\": \"Show\"}, {\"start\": 1, \"tag\": \"airport\", \"end\": 2, \"entity\": \"me\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Show me weather",
                            "case_converted_utterance": "Show me weather",
                            "mapping": "{\"tokens\": [\"Show\", \"me\", \"weather\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"MODE\", \"end\": 1, \"score\": 0.14623363065090153, \"entity\": \"Show\"}, {\"start\": 1, \"tag\": \"airport\", \"end\": 2, \"entity\": \"me\"}, {\"start\": 2, \"tag\": \"MODE\", \"end\": 3, \"score\": 0.10241400032170002, \"entity\": \"weather\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Whats weather",
                            "case_converted_utterance": "Whats weather",
                            "mapping": "{\"tokens\": [\"Whats\", \"weather\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"MODE\", \"end\": 1, \"score\": 0.11176551876495047, \"entity\": \"Whats\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Weather of a place",
                            "case_converted_utterance": "Weather of a place",
                            "mapping": "{\"tokens\": [\"Weather\", \"of\", \"a\", \"place\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.1381967649210164, \"entity\": \"Weather\"}, {\"start\": 3, \"tag\": \"TYPE\", \"end\": 4, \"score\": 0.1408800672112676, \"entity\": \"place\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Weather of London",
                            "case_converted_utterance": "Weather of London",
                            "mapping": "{\"tokens\": [\"Weather\", \"of\", \"London\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.1381967649210164, \"entity\": \"Weather\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Cochin weather",
                            "case_converted_utterance": "Cochin weather",
                            "mapping": "{\"tokens\": [\"Cochin\", \"weather\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.12158444891058733, \"entity\": \"Cochin\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Weather forcast",
                            "case_converted_utterance": "Weather forcast",
                            "mapping": "{\"tokens\": [\"Weather\", \"forcast\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.13702922069323892, \"entity\": \"Weather\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "What is the whether now for",
                            "case_converted_utterance": "What is the whether now for",
                            "mapping": "{\"tokens\": [\"What\", \"is\", \"the\", \"whether\", \"now\", \"for\"], \"text\": null, \"intent\": \"Weather\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "test here",
                            "case_converted_utterance": "Test here",
                            "mapping": "{\"tokens\": [\"Test\", \"here\"], \"text\": null, \"intent\": \"test1\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "No thanks",
                            "case_converted_utterance": "No thanks",
                            "mapping": "{\"tokens\": [\"No\", \"thanks\"], \"text\": null, \"intent\": \"conclusionflow\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "i want to book a travel ticket",
                            "case_converted_utterance": "I want to book a travel ticket",
                            "mapping": "{\"tokens\": [\"I\", \"want\", \"to\", \"book\", \"a\", \"travel\", \"ticket\"], \"text\": null, \"intent\": \"travelbooking\", \"tags\": [{\"start\": 5, \"tag\": \"type\", \"end\": 6, \"entity\": \"travel\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Hello how are you ",
                            "case_converted_utterance": "Hello how are you ",
                            "mapping": "{\"tokens\": [\"Hello\", \"how\", \"are\", \"you\"], \"text\": null, \"intent\": \"greetings\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Hi how are you ",
                            "case_converted_utterance": "Hi how are you ",
                            "mapping": "{\"tokens\": [\"Hi\", \"how\", \"are\", \"you\"], \"text\": null, \"intent\": \"greetings\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Book a ticket for me ",
                            "case_converted_utterance": "Book a ticket for me ",
                            "mapping": "{\"tokens\": [\"Book\", \"a\", \"ticket\", \"for\", \"me\"], \"text\": null, \"intent\": \"booking\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Please book a ticket ",
                            "case_converted_utterance": "Please book a ticket ",
                            "mapping": "{\"tokens\": [\"Please\", \"book\", \"a\", \"ticket\"], \"text\": null, \"intent\": \"booking\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Hello there ",
                            "case_converted_utterance": "Hello there ",
                            "mapping": "{\"tokens\": [\"Hello\", \"there\"], \"text\": null, \"intent\": \"greetings\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Hello ",
                            "case_converted_utterance": "Hello ",
                            "mapping": "{\"tokens\": [\"Hello\"], \"text\": null, \"intent\": \"greetings\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Anybody there ",
                            "case_converted_utterance": "Anybody there ",
                            "mapping": "{\"tokens\": [\"Anybody\", \"there\"], \"text\": null, \"intent\": \"greetings\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Hi there ",
                            "case_converted_utterance": "Hi there ",
                            "mapping": "{\"tokens\": [\"Hi\", \"there\"], \"text\": null, \"intent\": \"greetings\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Hi ",
                            "case_converted_utterance": "Hi ",
                            "mapping": "{\"tokens\": [\"Hi\"], \"text\": null, \"intent\": \"greetings\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Movie ",
                            "case_converted_utterance": "Movie ",
                            "mapping": "{\"tokens\": [\"Movie\"], \"text\": null, \"intent\": \"moviebooking\", \"tags\": [{\"start\": 0, \"tag\": \"type\", \"end\": 1, \"entity\": \"Movie\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Please make a movie booking ",
                            "case_converted_utterance": "Please make a movie booking ",
                            "mapping": "{\"tokens\": [\"Please\", \"make\", \"a\", \"movie\", \"booking\"], \"text\": null, \"intent\": \"moviebooking\", \"tags\": [{\"start\": 3, \"tag\": \"type\", \"end\": 4, \"entity\": \"movie\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "No please ",
                            "case_converted_utterance": "No please ",
                            "mapping": "{\"tokens\": [\"No\", \"please\"], \"text\": null, \"intent\": \"conclusion\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Good thanks ",
                            "case_converted_utterance": "Good thanks ",
                            "mapping": "{\"tokens\": [\"Good\", \"thanks\"], \"text\": null, \"intent\": \"conclusion\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Thanks I am good ",
                            "case_converted_utterance": "Thanks I am good ",
                            "mapping": "{\"tokens\": [\"Thanks\", \"I\", \"am\", \"good\"], \"text\": null, \"intent\": \"conclusion\", \"tags\": [{\"start\": 0, \"tag\": \"sample\", \"end\": 3, \"entity\": \"Thanks I am\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "No thanks ",
                            "case_converted_utterance": "No thanks ",
                            "mapping": "{\"tokens\": [\"No\", \"thanks\"], \"text\": null, \"intent\": \"conclusion\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Go ahead ",
                            "case_converted_utterance": "Go ahead ",
                            "mapping": "{\"tokens\": [\"Go\", \"ahead\"], \"text\": null, \"intent\": \"successflow\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Yes ",
                            "case_converted_utterance": "Yes ",
                            "mapping": "{\"tokens\": [\"Yes\"], \"text\": null, \"intent\": \"successflow\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Sure ",
                            "case_converted_utterance": "Sure ",
                            "mapping": "{\"tokens\": [\"Sure\"], \"text\": null, \"intent\": \"successflow\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Ok sure ",
                            "case_converted_utterance": "Ok sure ",
                            "mapping": "{\"tokens\": [\"Ok\", \"sure\"], \"text\": null, \"intent\": \"successflow\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Please go ahead ",
                            "case_converted_utterance": "Please go ahead ",
                            "mapping": "{\"tokens\": [\"Please\", \"go\", \"ahead\"], \"text\": null, \"intent\": \"successflow\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Yes please ",
                            "case_converted_utterance": "Yes please ",
                            "mapping": "{\"tokens\": [\"Yes\", \"please\"], \"text\": null, \"intent\": \"successflow\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Please do a travel booking ",
                            "case_converted_utterance": "Please do a travel booking ",
                            "mapping": "{\"tokens\": [\"Please\", \"do\", \"a\", \"travel\", \"booking\"], \"text\": null, \"intent\": \"travelbooking\", \"tags\": [{\"start\": 3, \"tag\": \"type\", \"end\": 4, \"entity\": \"travel\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Please do a booking ",
                            "case_converted_utterance": "Please do a booking ",
                            "mapping": "{\"tokens\": [\"Please\", \"do\", \"a\", \"booking\"], \"text\": null, \"intent\": \"booking\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "I want to make a travel booking ",
                            "case_converted_utterance": "I want to make a travel booking ",
                            "mapping": "{\"tokens\": [\"I\", \"want\", \"to\", \"make\", \"a\", \"travel\", \"booking\"], \"text\": null, \"intent\": \"travelbooking\", \"tags\": [{\"start\": 5, \"tag\": \"type\", \"end\": 6, \"entity\": \"travel\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "Please help in booking a travel ",
                            "case_converted_utterance": "Please help in booking a travel ",
                            "mapping": "{\"tokens\": [\"Please\", \"help\", \"in\", \"booking\", \"a\", \"travel\"], \"text\": null, \"intent\": \"travelbooking\", \"tags\": [{\"start\": 5, \"tag\": \"type\", \"end\": 6, \"entity\": \"travel\"}]}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "I want to make a booking ",
                            "case_converted_utterance": "I want to make a booking ",
                            "mapping": "{\"tokens\": [\"I\", \"want\", \"to\", \"make\", \"a\", \"booking\"], \"text\": null, \"intent\": \"booking\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        },
                        {
                            "utterance": "I would like to make a booking ",
                            "case_converted_utterance": "I would like to make a booking ",
                            "mapping": "{\"tokens\": [\"I\", \"would\", \"like\", \"to\", \"make\", \"a\", \"booking\"], \"text\": null, \"intent\": \"booking\", \"tags\": []}",
                            "ir_trained": false,
                            "ner_trained": false
                        }
                    ],
                    "id": "RGF0YXNvdXJjZTo1ZDA3NTJlZjMwOGFhZTZhMTE5YWU0Mjc=",
                    "serviceid": "0AoI5SB5ILHozOHzl8f5wS5skmejKfp9GcTVayQiYFsCldHPJA1qD4RleUBJfga5",
                    "entities": [
                        "type",
                        "mode",
                        "travelcount",
                        "bagsize",
                        "SAMPLE1"
                    ],
                    "intents": [
                        {
                            "name": "No intent",
                            "description": "Add the utterances that should not be labelled as any of your intents here.",
                            "createdAt": "2019-06-17T08:44:31.450Z",
                            "modifiedAt": "2019-06-17T08:44:31.450Z"
                        },
                        {
                            "name": "Greeting",
                            "description": "Marks the beginning of a conversation",
                            "createdAt": "2018-11-20T05:37:51.070Z",
                            "modifiedAt": "2018-11-20T05:37:51.070Z"
                        },
                        {
                            "name": "Weather",
                            "description": "Indicates that the user wants to know about the weather",
                            "createdAt": "2018-11-01T09:10:42.935Z",
                            "modifiedAt": "2018-11-01T09:10:42.935Z"
                        },
                        {
                            "name": "test1",
                            "description": "test",
                            "createdAt": "2018-11-01T09:10:08.712Z",
                            "modifiedAt": "2018-11-01T09:10:08.712Z"
                        },
                        {
                            "name": "booking",
                            "description": "booking",
                            "createdAt": "2018-11-01T08:44:06.846Z",
                            "modifiedAt": "2018-11-01T08:44:06.846Z"
                        },
                        {
                            "name": "travelbooking",
                            "description": "travelbooking",
                            "createdAt": "2018-10-25T09:21:34.482Z",
                            "modifiedAt": "2018-10-25T09:21:34.482Z"
                        },
                        {
                            "name": "greetings",
                            "description": "greetings",
                            "createdAt": "2018-10-25T09:21:34.482Z",
                            "modifiedAt": "2018-10-25T09:21:34.482Z"
                        },
                        {
                            "name": "conclusion",
                            "description": "conclusion",
                            "createdAt": "2018-10-25T09:21:34.482Z",
                            "modifiedAt": "2018-10-25T09:21:34.482Z"
                        },
                        {
                            "name": "successflow",
                            "description": "successflow",
                            "createdAt": "2018-10-25T09:21:34.482Z",
                            "modifiedAt": "2018-10-25T09:21:34.482Z"
                        },
                        {
                            "name": "moviebooking",
                            "description": "moviebooking",
                            "createdAt": "2018-10-25T09:21:34.482Z",
                            "modifiedAt": "2018-10-25T09:21:34.482Z"
                        },
                        {
                            "name": "airlinesearch",
                            "description": "airlinesearch",
                            "createdAt": "2018-10-25T09:21:34.482Z",
                            "modifiedAt": "2018-10-25T09:21:34.482Z"
                        },
                        {
                            "name": "airlinebooking",
                            "description": "airlinebooking",
                            "createdAt": "2018-10-25T09:21:34.482Z",
                            "modifiedAt": "2018-10-25T09:21:34.482Z"
                        },
                        {
                            "name": "conclusionflow",
                            "description": "conclusionflow",
                            "createdAt": "2018-10-25T09:21:34.482Z",
                            "modifiedAt": "2018-10-25T09:21:34.482Z"
                        },
                        {
                            "name": "AgentTranserRequest",
                            "description": "AgentTranserRequest",
                            "createdAt": "2018-11-20T04:33:56.486Z",
                            "modifiedAt": "2018-11-20T04:33:56.486Z"
                        },
                        {
                            "name": "AgentTransfer",
                            "description": "AgentTransfer",
                            "createdAt": "2018-11-20T04:34:28.500Z",
                            "modifiedAt": "2018-11-20T04:34:28.500Z"
                        }
                    ],
                    "trainIntent": true,
                    "trainEntity": true,
                    "predefined_entities": [],
                    "patterns": [
                        {
                            "pattern": "\\d{4}\\s/\\s\\d{2}\\s/\\s\\d{2}|\\d{2}\\s/\\s\\d{2}\\s/\\s\\d{4}",
                            "entity": "CUSTOM_DATE"
                        },
                        {
                            "pattern": "[0-9A-Z, ]{3,6}",
                            "entity": "sample"
                        },
                        {
                            "pattern": "[a-z0-9A-Z_.-]+@[da-zA-Z.-]+.[a-zA-Z.]{2,6}",
                            "entity": "email"
                        }
                    ],
                    "phrases": [
                        {
                            "phrase": [
                                "AL",
                                "BHM",
                                "DHN",
                                "HSV",
                                "MOB",
                                "MGM",
                                "AK",
                                "ANC",
                                "FAI",
                                "JNU",
                                "AZ",
                                "FLG",
                                "PHX",
                                "TUS",
                                "YUM",
                                "AR",
                                "FYV",
                                "LIT",
                                "CA",
                                "BUR",
                                "FAT",
                                "LGB",
                                "LAX",
                                "OAK",
                                "ONT",
                                "PSP",
                                "SMF",
                                "SAN",
                                "SFO",
                                "SJC",
                                "SNA",
                                "CO",
                                "ASE",
                                "COS",
                                "DEN",
                                "GJT",
                                "PUB",
                                "CT",
                                "BDL",
                                "DC",
                                "IAD",
                                "DCA",
                                "FL",
                                "DAB",
                                "FLL",
                                "RSW",
                                "JAX",
                                "EYW",
                                "MIA",
                                "MCO",
                                "PNS",
                                "PIE",
                                "SRQ",
                                "TPA",
                                "PBI",
                                "PFN",
                                "GA",
                                "ATL",
                                "AGS",
                                "SAV",
                                "HI01",
                                "ITO",
                                "HNL",
                                "OGG",
                                "KOA",
                                "LIH",
                                "ID",
                                "BOI",
                                "IL",
                                "MDW",
                                "ORD",
                                "MLI",
                                "PIA",
                                "EVV",
                                "FWA",
                                "IND",
                                "SBN",
                                "IA",
                                "CID",
                                "DSM",
                                "KS",
                                "ICT",
                                "KY",
                                "LEX",
                                "SDF",
                                "LA",
                                "BTR",
                                "MSY",
                                "SHV",
                                "ME",
                                "AUG",
                                "BGR",
                                "PWM",
                                "MD",
                                "BWI",
                                "MA",
                                "BOS",
                                "HYA",
                                "ACK",
                                "ORH",
                                "MI",
                                "BTL",
                                "DTW",
                                "DET",
                                "FNT",
                                "GRR",
                                "AZO",
                                "LAN",
                                "MBS",
                                "MN",
                                "DLH",
                                "MSP",
                                "RST",
                                "MS",
                                "GPT",
                                "JAN",
                                "MO",
                                "MCI",
                                "STL",
                                "SGF",
                                "MT",
                                "BIL",
                                "NE",
                                "LNK",
                                "OMA",
                                "NV",
                                "LAS",
                                "RNO",
                                "NH",
                                "MHT",
                                "NJ",
                                "ACY",
                                "EWR",
                                "TTN",
                                "NM",
                                "ABQ",
                                "ALM",
                                "NY",
                                "ALB",
                                "BUF",
                                "ISP",
                                "JFK",
                                "LGA",
                                "SWF",
                                "ROC",
                                "SYR",
                                "HPN",
                                "NC",
                                "AVL",
                                "CLT",
                                "FAY",
                                "GSO",
                                "RDU",
                                "INT",
                                "ND",
                                "BIS",
                                "FAR",
                                "OH",
                                "CAK",
                                "CVG",
                                "CLE",
                                "CMH",
                                "DAY",
                                "TOL",
                                "OKC",
                                "TUL",
                                "OR",
                                "EUG",
                                "PDX",
                                "HIO",
                                "SLE",
                                "PA",
                                "ABE",
                                "ERI",
                                "MDT",
                                "PHL",
                                "PIT",
                                "AVP",
                                "RI",
                                "PVD",
                                "SC",
                                "CHS",
                                "CAE",
                                "GSP",
                                "MYR",
                                "SD",
                                "PIR",
                                "RAP",
                                "FSD",
                                "TN",
                                "TRI",
                                "CHA",
                                "TYS",
                                "MEM",
                                "BNA",
                                "TX",
                                "AMA",
                                "AUS",
                                "CRP",
                                "DAL",
                                "DFW",
                                "ELP",
                                "HOU",
                                "IAH",
                                "LBB",
                                "MAF",
                                "SAT",
                                "UT",
                                "SLC",
                                "VT",
                                "BTV",
                                "MPV",
                                "RUT",
                                "VA",
                                "IAD",
                                "PHF",
                                "ORF",
                                "RIC",
                                "ROA",
                                "WA",
                                "PSC",
                                "SEA",
                                "GEG",
                                "WV",
                                "CRW",
                                "CKB",
                                "WI",
                                "GRB",
                                "MSN",
                                "MKE",
                                "WY",
                                "CPR",
                                "CYS",
                                "JAC",
                                "RKS"
                            ],
                            "entity": "airport"
                        },
                        {
                            "phrase": [
                                "US1423",
                                "AA1234",
                                "AA0172",
                                "SP1000",
                                "DL2001",
                                "SW1414",
                                "AL9898",
                                "FR4331"
                            ],
                            "entity": "flightno"
                        },
                        {
                            "phrase": [
                                "Flight",
                                "air plane",
                                "aeroplane"
                            ],
                            "entity": "airtypes"
                        },
                        {
                            "phrase": [
                                "abc",
                                "def"
                            ],
                            "entity": "test2"
                        }
                    ],
                    "synonyms": []
                },
                "integration_markdown": "",
                "build_report": null
            }
        ]
    }
}

#####################################################################################################################

Delete Project:

Query:
const deleteProjectQuery = (projectId, configId) => `
  mutation {
    deleteProject: deleteProject(input: {id: "${projectId}"}){
      ok
    },

    delProjectConfig: deleteProjectConfig(input: {id: "${configId}"}){
      ok
    }
  }
`;

Request URL:
http://ice-xd.southindia.cloudapp.azure.com:3001/project/configure/5d022211308aae6a11956492
5d022211308aae6a11956492 is the project id

POST Data:

{id: "projectId"}

JSON Response:

{"data":{"deleteProject":{"ok":true},"delProjectConfig":{"ok":true}}}

#####################################################################################################################

Update Datasource:

Query:
const updateDatasourceQuery = `
  mutation UpdateDatasource($input: updateDatasourceInput!) {
    updateDatasource(input: $input) {
      changedDatasource {
         _id
         serviceid
         utterances{
           utterance
           case_converted_utterance
           mapping
           ir_trained
           ner_trained
         }
         entities
         intents{
           name
           description
           createdAt
           modifiedAt
         }
         trainEntity
         trainIntent
         predefined_entities
         patterns{
           pattern
           entity
         }
         phrases{
           phrase
           entity
         }
         synonyms{
           synonym
           word
         }
      }
    }
  }
`;

Request URL:
http://ice-xd.southindia.cloudapp.azure.com:3001/project/configure/5d0752ee308aae6a119ae425
5d0752ee308aae6a119ae425 is the project id

POST Data:
{
    "input": {
        "clientMutationId": "random",
        "entities": [
            "type",
            "mode",
            "travelcount",
            "bagsize",
            "SAMPLE1"
        ],
        "utterances": [
            {
                "utterance": "qqqq",
                "mapping": "{\"tokens\":[\"Qqqq\"],\"tags\":[{\"start\":0,\"tag\":\"sample\",\"end\":1,\"entity\":\"qqqq\"}],\"intent\":\"Weather\"}",
                "case_converted_utterance": "Qqqq"
            },
            {
                "utterance": "heyyy",
                "case_converted_utterance": "Heyyy",
                "mapping": "{\"tokens\":[\"Heyyy\"],\"tags\":[{\"start\":0,\"tag\":\"sample\",\"end\":1,\"entity\":\"heyyy\"}],\"intent\":\"test1\"}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "I want to do a travel",
                "case_converted_utterance": "I want to do a travel",
                "mapping": "{\"tokens\": [\"I\", \"want\", \"to\", \"do\", \"a\", \"travel\"], \"intent\": \"travelbooking\", \"tags\": [{\"start\": 5, \"tag\": \"TYPE\", \"end\": 6, \"score\": 0.5640399006298088, \"entity\": \"travel\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "travel booking",
                "case_converted_utterance": "Travel booking",
                "mapping": "{\"tokens\": [\"Travel\", \"booking\"], \"intent\": \"travelbooking\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.5286114190311912, \"entity\": \"travel\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "travel",
                "case_converted_utterance": "Travel",
                "mapping": "{\"tokens\": [\"Travel\"], \"intent\": \"travelbooking\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.2537922087668458, \"entity\": \"travel\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Please to a flight booking",
                "case_converted_utterance": "Please to a flight booking",
                "mapping": "{\"tokens\": [\"Please\", \"to\", \"a\", \"flight\", \"booking\"], \"intent\": \"airlinesearch\", \"tags\": [{\"start\": 3, \"tag\": \"mode\", \"end\": 4, \"entity\": \"flight\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "I would like to travel by flight",
                "case_converted_utterance": "I would like to travel by flight",
                "mapping": "{\"tokens\": [\"I\", \"would\", \"like\", \"to\", \"travel\", \"by\", \"flight\"], \"intent\": \"airlinesearch\", \"tags\": [{\"start\": 4, \"tag\": \"TYPE\", \"end\": 5, \"score\": 0.4979866350219423, \"entity\": \"travel\"}, {\"start\": 6, \"tag\": \"mode\", \"end\": 7, \"entity\": \"flight\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "kindly book one flight",
                "case_converted_utterance": "Kindly book one flight",
                "mapping": "{\"tokens\": [\"Kindly\", \"book\", \"one\", \"flight\"], \"intent\": \"airlinesearch\", \"tags\": [{\"start\": 3, \"tag\": \"mode\", \"end\": 4, \"entity\": \"flight\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "flight",
                "case_converted_utterance": "Flight",
                "mapping": "{\"tokens\": [\"Flight\"], \"intent\": \"airlinesearch\", \"tags\": [{\"start\": 0, \"tag\": \"mode\", \"end\": 1, \"entity\": \"flight\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Please book a flight ticket for me",
                "case_converted_utterance": "Please book a flight ticket for me",
                "mapping": "{\"tokens\": [\"Please\", \"book\", \"a\", \"flight\", \"ticket\", \"for\", \"me\"], \"intent\": \"airlinesearch\", \"tags\": [{\"start\": 0, \"tag\": \"mode\", \"end\": 1, \"entity\": \"\"}, {\"start\": 3, \"tag\": \"mode\", \"end\": 4, \"entity\": \"flight\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Please do a travel booking",
                "case_converted_utterance": "Please do a travel booking",
                "mapping": "{\"tokens\": [\"Please\", \"do\", \"a\", \"travel\", \"booking\"], \"intent\": \"travelbooking\", \"tags\": [{\"start\": 3, \"tag\": \"TYPE\", \"end\": 4, \"score\": 0.6740128800829303, \"entity\": \"travel\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "I want to travel",
                "case_converted_utterance": "I want to travel",
                "mapping": "{\"tokens\": [\"I\", \"want\", \"to\", \"travel\"], \"intent\": \"travelbooking\", \"tags\": [{\"start\": 3, \"tag\": \"TYPE\", \"end\": 4, \"score\": 0.3422346315669714, \"entity\": \"travel\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "I want travel",
                "case_converted_utterance": "I want travel",
                "mapping": "{\"tokens\": [\"I\", \"want\", \"travel\"], \"intent\": \"travelbooking\", \"tags\": [{\"start\": 2, \"tag\": \"TYPE\", \"end\": 3, \"score\": 0.23075157859533177, \"entity\": \"travel\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "I want to do booking",
                "case_converted_utterance": "I want to do booking",
                "mapping": "{\"tokens\": [\"I\", \"want\", \"to\", \"do\", \"booking\"], \"intent\": \"booking\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Please do a booking",
                "case_converted_utterance": "Please do a booking",
                "mapping": "{\"tokens\": [\"Please\", \"do\", \"a\", \"booking\"], \"intent\": \"booking\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Please booking",
                "case_converted_utterance": "Please booking",
                "mapping": "{\"tokens\": [\"Please\", \"booking\"], \"intent\": \"booking\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "I want to do a booking",
                "case_converted_utterance": "I want to do a booking",
                "mapping": "{\"tokens\": [\"I\", \"want\", \"to\", \"do\", \"a\", \"booking\"], \"intent\": \"booking\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "hiiii",
                "case_converted_utterance": "Hiiii",
                "mapping": "{\"tokens\": [\"Hiiii\"], \"intent\": \"Greeting\", \"tags\": [{\"start\": 0, \"tag\": \"MODE\", \"end\": 1, \"score\": 0.1243794318755859, \"entity\": \"hiiii\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "hi",
                "case_converted_utterance": "Hi",
                "mapping": "{\"tokens\": [\"Hi\"], \"intent\": \"Greeting\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "heyya",
                "case_converted_utterance": "Heyya",
                "mapping": "{\"tokens\": [\"Heyya\"], \"intent\": \"Greeting\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "hello",
                "case_converted_utterance": "Hello",
                "mapping": "{\"tokens\": [\"Hello\"], \"intent\": \"Greeting\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "hi",
                "case_converted_utterance": "Hi",
                "mapping": "{\"tokens\": [\"Hi\"], \"intent\": \"Greeting\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "You there",
                "case_converted_utterance": "You there",
                "mapping": "{\"tokens\": [\"You\", \"there\"], \"intent\": \"Greeting\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Hey",
                "case_converted_utterance": "Hey",
                "mapping": "{\"tokens\": [\"Hey\"], \"intent\": \"Greeting\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Hai",
                "case_converted_utterance": "Hai",
                "mapping": "{\"tokens\": [\"Hai\"], \"intent\": \"Greeting\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Hi",
                "case_converted_utterance": "Hi",
                "mapping": "{\"tokens\": [\"Hi\"], \"intent\": \"Greeting\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Good morning",
                "case_converted_utterance": "Good morning",
                "mapping": "{\"tokens\": [\"Good\", \"morning\"], \"intent\": \"Greeting\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.2530555062914658, \"entity\": \"Good\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Good day",
                "case_converted_utterance": "Good day",
                "mapping": "{\"tokens\": [\"Good\", \"day\"], \"intent\": \"Greeting\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.2684357011642687, \"entity\": \"Good\"}, {\"start\": 1, \"tag\": \"airport\", \"end\": 2, \"entity\": \"day\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Good evening",
                "case_converted_utterance": "Good evening",
                "mapping": "{\"tokens\": [\"Good\", \"evening\"], \"intent\": \"Greeting\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Hey twin",
                "case_converted_utterance": "Hey twin",
                "mapping": "{\"tokens\": [\"Hey\", \"twin\"], \"intent\": \"Greeting\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Hi there",
                "case_converted_utterance": "Hi there",
                "mapping": "{\"tokens\": [\"Hi\", \"there\"], \"intent\": \"Greeting\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "What'S up ?",
                "case_converted_utterance": "What'S up ?",
                "mapping": "{\"tokens\": [\"What'S\", \"up\", \"?\"], \"intent\": \"Greeting\", \"tags\": [{\"start\": 2, \"tag\": \"MODE\", \"end\": 3, \"score\": 0.3594824179203809, \"entity\": \"?\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Who is this ?",
                "case_converted_utterance": "Who is this ?",
                "mapping": "{\"tokens\": [\"Who\", \"is\", \"this\", \"?\"], \"intent\": \"Greeting\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "What'S new ?",
                "case_converted_utterance": "What'S new ?",
                "mapping": "{\"tokens\": [\"What'S\", \"new\", \"?\"], \"intent\": \"Greeting\", \"tags\": [{\"start\": 0, \"tag\": \"MODE\", \"end\": 1, \"score\": 0.276929868992718, \"entity\": \"What'S\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Hey there",
                "case_converted_utterance": "Hey there",
                "mapping": "{\"tokens\": [\"Hey\", \"there\"], \"intent\": \"Greeting\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Ok take me back",
                "case_converted_utterance": "Ok take me back",
                "mapping": "{\"tokens\": [\"Ok\", \"take\", \"me\", \"back\"], \"intent\": \"Greeting\", \"tags\": [{\"start\": 2, \"tag\": \"airport\", \"end\": 3, \"entity\": \"me\"}, {\"start\": 3, \"tag\": \"MODE\", \"end\": 4, \"score\": 0.28095878767074006, \"entity\": \"back\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Looking good eve",
                "case_converted_utterance": "Looking good eve",
                "mapping": "{\"tokens\": [\"Looking\", \"good\", \"eve\"], \"intent\": \"Greeting\", \"tags\": [{\"start\": 2, \"tag\": \"MODE\", \"end\": 3, \"score\": 0.3454258060185423, \"entity\": \"eve\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "How R U ?",
                "case_converted_utterance": "How R U ?",
                "mapping": "{\"tokens\": [\"How\", \"R\", \"U\", \"?\"], \"intent\": \"Greeting\", \"tags\": [{\"start\": 0, \"tag\": \"sample\", \"end\": 4, \"entity\": \"How R U ?\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "How is it going ?",
                "case_converted_utterance": "How is it going ?",
                "mapping": "{\"tokens\": [\"How\", \"is\", \"it\", \"going\", \"?\"], \"intent\": \"Greeting\", \"tags\": [{\"start\": 4, \"tag\": \"MODE\", \"end\": 5, \"score\": 0.22077778757291347, \"entity\": \"?\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "How have you been ?",
                "case_converted_utterance": "How have you been ?",
                "mapping": "{\"tokens\": [\"How\", \"have\", \"you\", \"been\", \"?\"], \"intent\": \"Greeting\", \"tags\": [{\"start\": 4, \"tag\": \"MODE\", \"end\": 5, \"score\": 0.21941104933103223, \"entity\": \"?\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "How are you today ?",
                "case_converted_utterance": "How are you today ?",
                "mapping": "{\"tokens\": [\"How\", \"are\", \"you\", \"today\", \"?\"], \"intent\": \"Greeting\", \"tags\": [{\"start\": 4, \"tag\": \"MODE\", \"end\": 5, \"score\": 0.22229289284995607, \"entity\": \"?\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "How are things going ?",
                "case_converted_utterance": "How are things going ?",
                "mapping": "{\"tokens\": [\"How\", \"are\", \"things\", \"going\", \"?\"], \"intent\": \"Greeting\", \"tags\": [{\"start\": 4, \"tag\": \"MODE\", \"end\": 5, \"score\": 0.22077778757291347, \"entity\": \"?\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Hello I am looking for some help here",
                "case_converted_utterance": "Hello I am looking for some help here",
                "mapping": "{\"tokens\": [\"Hello\", \"I\", \"am\", \"looking\", \"for\", \"some\", \"help\", \"here\"], \"intent\": \"Greeting\", \"tags\": [{\"start\": 0, \"tag\": \"sample\", \"end\": 3, \"entity\": \"Hello I am\"}, {\"start\": 6, \"tag\": \"TYPE\", \"end\": 7, \"score\": 0.11152091750581689, \"entity\": \"help\"}, {\"start\": 7, \"tag\": \"MODE\", \"end\": 8, \"score\": 0.21238762326047897, \"entity\": \"here\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Hi advisor",
                "case_converted_utterance": "Hi advisor",
                "mapping": "{\"tokens\": [\"Hi\", \"advisor\"], \"intent\": \"Greeting\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Hey you",
                "case_converted_utterance": "Hey you",
                "mapping": "{\"tokens\": [\"Hey\", \"you\"], \"intent\": \"Greeting\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Hey there all",
                "case_converted_utterance": "Hey there all",
                "mapping": "{\"tokens\": [\"Hey\", \"there\", \"all\"], \"intent\": \"Greeting\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Hey how are you doing",
                "case_converted_utterance": "Hey how are you doing",
                "mapping": "{\"tokens\": [\"Hey\", \"how\", \"are\", \"you\", \"doing\"], \"intent\": \"Greeting\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Hello",
                "case_converted_utterance": "Hello",
                "mapping": "{\"tokens\": [\"Hello\"], \"intent\": \"Greeting\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Hello agent",
                "case_converted_utterance": "Hello agent",
                "mapping": "{\"tokens\": [\"Hello\", \"agent\"], \"intent\": \"Greeting\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Have you been well ?",
                "case_converted_utterance": "Have you been well ?",
                "mapping": "{\"tokens\": [\"Have\", \"you\", \"been\", \"well\", \"?\"], \"intent\": \"Greeting\", \"tags\": [{\"start\": 2, \"tag\": \"MODE\", \"end\": 3, \"score\": 0.2390684494907248, \"entity\": \"been\"}, {\"start\": 4, \"tag\": \"MODE\", \"end\": 5, \"score\": 0.2158975453646159, \"entity\": \"?\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Greetings",
                "case_converted_utterance": "Greetings",
                "mapping": "{\"tokens\": [\"Greetings\"], \"intent\": \"Greeting\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Good to see you",
                "case_converted_utterance": "Good to see you",
                "mapping": "{\"tokens\": [\"Good\", \"to\", \"see\", \"you\"], \"intent\": \"Greeting\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "no",
                "case_converted_utterance": "No",
                "mapping": "{\"tokens\": [\"No\"], \"intent\": \"conclusionflow\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "no thank you",
                "case_converted_utterance": "No thank you",
                "mapping": "{\"tokens\": [\"No\", \"thank\", \"you\"], \"intent\": \"conclusionflow\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "hello",
                "case_converted_utterance": "Hello",
                "mapping": "{\"tokens\": [\"Hello\"], \"intent\": \"test1\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "23394 weather",
                "case_converted_utterance": "23394 weather",
                "mapping": "{\"tokens\": [\"23394\", \"weather\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"sample\", \"end\": 2, \"entity\": \"23394 weather\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Weather of 23294",
                "case_converted_utterance": "Weather of 23294",
                "mapping": "{\"tokens\": [\"Weather\", \"of\", \"23294\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.1381967649210164, \"entity\": \"Weather\"}, {\"start\": 1, \"tag\": \"sample\", \"end\": 3, \"entity\": \"of 23294\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Temperature of 695024",
                "case_converted_utterance": "Temperature of 695024",
                "mapping": "{\"tokens\": [\"Temperature\", \"of\", \"695024\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.11583915744592144, \"entity\": \"Temperature\"}, {\"start\": 1, \"tag\": \"sample\", \"end\": 3, \"entity\": \"of 695024\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Temperature of Manchester",
                "case_converted_utterance": "Temperature of Manchester",
                "mapping": "{\"tokens\": [\"Temperature\", \"of\", \"Manchester\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.11583915744592144, \"entity\": \"Temperature\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Weather of La",
                "case_converted_utterance": "Weather of La",
                "mapping": "{\"tokens\": [\"Weather\", \"of\", \"La\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.1381967649210164, \"entity\": \"Weather\"}, {\"start\": 2, \"tag\": \"airport\", \"end\": 3, \"entity\": \"La\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Zzzz 0Zz weather",
                "case_converted_utterance": "Zzzz 0Zz weather",
                "mapping": "{\"tokens\": [\"Zzzz\", \"0Zz\", \"weather\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"sample\", \"end\": 2, \"entity\": \"Zzzz 0Zz\"}, {\"start\": 2, \"tag\": \"MODE\", \"end\": 3, \"score\": 0.10199896814355316, \"entity\": \"weather\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Weather of XXXX XXX",
                "case_converted_utterance": "Weather of XXXX XXX",
                "mapping": "{\"tokens\": [\"Weather\", \"of\", \"XXXX\", \"XXX\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.1381967649210164, \"entity\": \"Weather\"}, {\"start\": 1, \"tag\": \"sample\", \"end\": 4, \"entity\": \"of XXXX XXX\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "99900 weather",
                "case_converted_utterance": "99900 weather",
                "mapping": "{\"tokens\": [\"99900\", \"weather\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"sample\", \"end\": 2, \"entity\": \"99900 weather\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Trivandrum weather",
                "case_converted_utterance": "Trivandrum weather",
                "mapping": "{\"tokens\": [\"Trivandrum\", \"weather\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.10129349747641157, \"entity\": \"Trivandrum\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Weather of Trivandrum",
                "case_converted_utterance": "Weather of Trivandrum",
                "mapping": "{\"tokens\": [\"Weather\", \"of\", \"Trivandrum\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.1381967649210164, \"entity\": \"Weather\"}, {\"start\": 2, \"tag\": \"MODE\", \"end\": 3, \"score\": 0.12936659812427925, \"entity\": \"Trivandrum\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Temperature of Trivandrum",
                "case_converted_utterance": "Temperature of Trivandrum",
                "mapping": "{\"tokens\": [\"Temperature\", \"of\", \"Trivandrum\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.11583915744592144, \"entity\": \"Temperature\"}, {\"start\": 2, \"tag\": \"MODE\", \"end\": 3, \"score\": 0.12936659812427925, \"entity\": \"Trivandrum\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Climate of Trivandrum",
                "case_converted_utterance": "Climate of Trivandrum",
                "mapping": "{\"tokens\": [\"Climate\", \"of\", \"Trivandrum\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.109057259808529, \"entity\": \"Climate\"}, {\"start\": 2, \"tag\": \"MODE\", \"end\": 3, \"score\": 0.12936659812427925, \"entity\": \"Trivandrum\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Show me weather of Chennai",
                "case_converted_utterance": "Show me weather of Chennai",
                "mapping": "{\"tokens\": [\"Show\", \"me\", \"weather\", \"of\", \"Chennai\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"MODE\", \"end\": 1, \"score\": 0.14623363065090153, \"entity\": \"Show\"}, {\"start\": 1, \"tag\": \"airport\", \"end\": 2, \"entity\": \"me\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Show me weather",
                "case_converted_utterance": "Show me weather",
                "mapping": "{\"tokens\": [\"Show\", \"me\", \"weather\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"MODE\", \"end\": 1, \"score\": 0.14623363065090153, \"entity\": \"Show\"}, {\"start\": 1, \"tag\": \"airport\", \"end\": 2, \"entity\": \"me\"}, {\"start\": 2, \"tag\": \"MODE\", \"end\": 3, \"score\": 0.10241400032170002, \"entity\": \"weather\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Whats weather",
                "case_converted_utterance": "Whats weather",
                "mapping": "{\"tokens\": [\"Whats\", \"weather\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"MODE\", \"end\": 1, \"score\": 0.11176551876495047, \"entity\": \"Whats\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Weather of a place",
                "case_converted_utterance": "Weather of a place",
                "mapping": "{\"tokens\": [\"Weather\", \"of\", \"a\", \"place\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.1381967649210164, \"entity\": \"Weather\"}, {\"start\": 3, \"tag\": \"TYPE\", \"end\": 4, \"score\": 0.1408800672112676, \"entity\": \"place\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Weather of London",
                "case_converted_utterance": "Weather of London",
                "mapping": "{\"tokens\": [\"Weather\", \"of\", \"London\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.1381967649210164, \"entity\": \"Weather\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Cochin weather",
                "case_converted_utterance": "Cochin weather",
                "mapping": "{\"tokens\": [\"Cochin\", \"weather\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.12158444891058733, \"entity\": \"Cochin\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Weather forcast",
                "case_converted_utterance": "Weather forcast",
                "mapping": "{\"tokens\": [\"Weather\", \"forcast\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.13702922069323892, \"entity\": \"Weather\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "What is the whether now for",
                "case_converted_utterance": "What is the whether now for",
                "mapping": "{\"tokens\": [\"What\", \"is\", \"the\", \"whether\", \"now\", \"for\"], \"text\": null, \"intent\": \"Weather\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "test here",
                "case_converted_utterance": "Test here",
                "mapping": "{\"tokens\": [\"Test\", \"here\"], \"text\": null, \"intent\": \"test1\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "No thanks",
                "case_converted_utterance": "No thanks",
                "mapping": "{\"tokens\": [\"No\", \"thanks\"], \"text\": null, \"intent\": \"conclusionflow\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "i want to book a travel ticket",
                "case_converted_utterance": "I want to book a travel ticket",
                "mapping": "{\"tokens\": [\"I\", \"want\", \"to\", \"book\", \"a\", \"travel\", \"ticket\"], \"text\": null, \"intent\": \"travelbooking\", \"tags\": [{\"start\": 5, \"tag\": \"type\", \"end\": 6, \"entity\": \"travel\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Hello how are you ",
                "case_converted_utterance": "Hello how are you ",
                "mapping": "{\"tokens\": [\"Hello\", \"how\", \"are\", \"you\"], \"text\": null, \"intent\": \"greetings\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Hi how are you ",
                "case_converted_utterance": "Hi how are you ",
                "mapping": "{\"tokens\": [\"Hi\", \"how\", \"are\", \"you\"], \"text\": null, \"intent\": \"greetings\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Book a ticket for me ",
                "case_converted_utterance": "Book a ticket for me ",
                "mapping": "{\"tokens\": [\"Book\", \"a\", \"ticket\", \"for\", \"me\"], \"text\": null, \"intent\": \"booking\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Please book a ticket ",
                "case_converted_utterance": "Please book a ticket ",
                "mapping": "{\"tokens\": [\"Please\", \"book\", \"a\", \"ticket\"], \"text\": null, \"intent\": \"booking\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Hello there ",
                "case_converted_utterance": "Hello there ",
                "mapping": "{\"tokens\": [\"Hello\", \"there\"], \"text\": null, \"intent\": \"greetings\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Hello ",
                "case_converted_utterance": "Hello ",
                "mapping": "{\"tokens\": [\"Hello\"], \"text\": null, \"intent\": \"greetings\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Anybody there ",
                "case_converted_utterance": "Anybody there ",
                "mapping": "{\"tokens\": [\"Anybody\", \"there\"], \"text\": null, \"intent\": \"greetings\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Hi there ",
                "case_converted_utterance": "Hi there ",
                "mapping": "{\"tokens\": [\"Hi\", \"there\"], \"text\": null, \"intent\": \"greetings\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Hi ",
                "case_converted_utterance": "Hi ",
                "mapping": "{\"tokens\": [\"Hi\"], \"text\": null, \"intent\": \"greetings\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Movie ",
                "case_converted_utterance": "Movie ",
                "mapping": "{\"tokens\": [\"Movie\"], \"text\": null, \"intent\": \"moviebooking\", \"tags\": [{\"start\": 0, \"tag\": \"type\", \"end\": 1, \"entity\": \"Movie\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Please make a movie booking ",
                "case_converted_utterance": "Please make a movie booking ",
                "mapping": "{\"tokens\": [\"Please\", \"make\", \"a\", \"movie\", \"booking\"], \"text\": null, \"intent\": \"moviebooking\", \"tags\": [{\"start\": 3, \"tag\": \"type\", \"end\": 4, \"entity\": \"movie\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "No please ",
                "case_converted_utterance": "No please ",
                "mapping": "{\"tokens\": [\"No\", \"please\"], \"text\": null, \"intent\": \"conclusion\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Good thanks ",
                "case_converted_utterance": "Good thanks ",
                "mapping": "{\"tokens\": [\"Good\", \"thanks\"], \"text\": null, \"intent\": \"conclusion\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Thanks I am good ",
                "case_converted_utterance": "Thanks I am good ",
                "mapping": "{\"tokens\": [\"Thanks\", \"I\", \"am\", \"good\"], \"text\": null, \"intent\": \"conclusion\", \"tags\": [{\"start\": 0, \"tag\": \"sample\", \"end\": 3, \"entity\": \"Thanks I am\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "No thanks ",
                "case_converted_utterance": "No thanks ",
                "mapping": "{\"tokens\": [\"No\", \"thanks\"], \"text\": null, \"intent\": \"conclusion\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Go ahead ",
                "case_converted_utterance": "Go ahead ",
                "mapping": "{\"tokens\": [\"Go\", \"ahead\"], \"text\": null, \"intent\": \"successflow\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Yes ",
                "case_converted_utterance": "Yes ",
                "mapping": "{\"tokens\": [\"Yes\"], \"text\": null, \"intent\": \"successflow\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Sure ",
                "case_converted_utterance": "Sure ",
                "mapping": "{\"tokens\": [\"Sure\"], \"text\": null, \"intent\": \"successflow\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Ok sure ",
                "case_converted_utterance": "Ok sure ",
                "mapping": "{\"tokens\": [\"Ok\", \"sure\"], \"text\": null, \"intent\": \"successflow\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Please go ahead ",
                "case_converted_utterance": "Please go ahead ",
                "mapping": "{\"tokens\": [\"Please\", \"go\", \"ahead\"], \"text\": null, \"intent\": \"successflow\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Yes please ",
                "case_converted_utterance": "Yes please ",
                "mapping": "{\"tokens\": [\"Yes\", \"please\"], \"text\": null, \"intent\": \"successflow\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Please do a travel booking ",
                "case_converted_utterance": "Please do a travel booking ",
                "mapping": "{\"tokens\": [\"Please\", \"do\", \"a\", \"travel\", \"booking\"], \"text\": null, \"intent\": \"travelbooking\", \"tags\": [{\"start\": 3, \"tag\": \"type\", \"end\": 4, \"entity\": \"travel\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Please do a booking ",
                "case_converted_utterance": "Please do a booking ",
                "mapping": "{\"tokens\": [\"Please\", \"do\", \"a\", \"booking\"], \"text\": null, \"intent\": \"booking\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "I want to make a travel booking ",
                "case_converted_utterance": "I want to make a travel booking ",
                "mapping": "{\"tokens\": [\"I\", \"want\", \"to\", \"make\", \"a\", \"travel\", \"booking\"], \"text\": null, \"intent\": \"travelbooking\", \"tags\": [{\"start\": 5, \"tag\": \"type\", \"end\": 6, \"entity\": \"travel\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "Please help in booking a travel ",
                "case_converted_utterance": "Please help in booking a travel ",
                "mapping": "{\"tokens\": [\"Please\", \"help\", \"in\", \"booking\", \"a\", \"travel\"], \"text\": null, \"intent\": \"travelbooking\", \"tags\": [{\"start\": 5, \"tag\": \"type\", \"end\": 6, \"entity\": \"travel\"}]}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "I want to make a booking ",
                "case_converted_utterance": "I want to make a booking ",
                "mapping": "{\"tokens\": [\"I\", \"want\", \"to\", \"make\", \"a\", \"booking\"], \"text\": null, \"intent\": \"booking\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            },
            {
                "utterance": "I would like to make a booking ",
                "case_converted_utterance": "I would like to make a booking ",
                "mapping": "{\"tokens\": [\"I\", \"would\", \"like\", \"to\", \"make\", \"a\", \"booking\"], \"text\": null, \"intent\": \"booking\", \"tags\": []}",
                "ir_trained": false,
                "ner_trained": false
            }
        ],
        "patterns": [
            {
                "pattern": "\\d{4}\\s/\\s\\d{2}\\s/\\s\\d{2}|\\d{2}\\s/\\s\\d{2}\\s/\\s\\d{4}",
                "entity": "CUSTOM_DATE"
            },
            {
                "pattern": "[0-9A-Z, ]{3,6}",
                "entity": "sample"
            },
            {
                "pattern": "[a-z0-9A-Z_.-]+@[da-zA-Z.-]+.[a-zA-Z.]{2,6}",
                "entity": "email"
            }
        ],
        "trainIntent": true,
        "trainEntity": true,
        "serviceid": "0AoI5SB5ILHozOHzl8f5wS5skmejKfp9GcTVayQiYFsCldHPJA1qD4RleUBJfga5",
        "intents": [
            {
                "name": "No intent",
                "description": "Add the utterances that should not be labelled as any of your intents here.",
                "createdAt": "2019-06-17T08:44:31.450Z",
                "modifiedAt": "2019-06-17T08:44:31.450Z"
            },
            {
                "name": "Greeting",
                "description": "Marks the beginning of a conversation",
                "createdAt": "2018-11-20T05:37:51.070Z",
                "modifiedAt": "2018-11-20T05:37:51.070Z"
            },
            {
                "name": "Weather",
                "description": "Indicates that the user wants to know about the weather",
                "createdAt": "2018-11-01T09:10:42.935Z",
                "modifiedAt": "2018-11-01T09:10:42.935Z"
            },
            {
                "name": "test1",
                "description": "test",
                "createdAt": "2018-11-01T09:10:08.712Z",
                "modifiedAt": "2018-11-01T09:10:08.712Z"
            },
            {
                "name": "booking",
                "description": "booking",
                "createdAt": "2018-11-01T08:44:06.846Z",
                "modifiedAt": "2018-11-01T08:44:06.846Z"
            },
            {
                "name": "travelbooking",
                "description": "travelbooking",
                "createdAt": "2018-10-25T09:21:34.482Z",
                "modifiedAt": "2018-10-25T09:21:34.482Z"
            },
            {
                "name": "greetings",
                "description": "greetings",
                "createdAt": "2018-10-25T09:21:34.482Z",
                "modifiedAt": "2018-10-25T09:21:34.482Z"
            },
            {
                "name": "conclusion",
                "description": "conclusion",
                "createdAt": "2018-10-25T09:21:34.482Z",
                "modifiedAt": "2018-10-25T09:21:34.482Z"
            },
            {
                "name": "successflow",
                "description": "successflow",
                "createdAt": "2018-10-25T09:21:34.482Z",
                "modifiedAt": "2018-10-25T09:21:34.482Z"
            },
            {
                "name": "moviebooking",
                "description": "moviebooking",
                "createdAt": "2018-10-25T09:21:34.482Z",
                "modifiedAt": "2018-10-25T09:21:34.482Z"
            },
            {
                "name": "airlinesearch",
                "description": "airlinesearch",
                "createdAt": "2018-10-25T09:21:34.482Z",
                "modifiedAt": "2018-10-25T09:21:34.482Z"
            },
            {
                "name": "airlinebooking",
                "description": "airlinebooking",
                "createdAt": "2018-10-25T09:21:34.482Z",
                "modifiedAt": "2018-10-25T09:21:34.482Z"
            },
            {
                "name": "conclusionflow",
                "description": "conclusionflow",
                "createdAt": "2018-10-25T09:21:34.482Z",
                "modifiedAt": "2018-10-25T09:21:34.482Z"
            },
            {
                "name": "AgentTranserRequest",
                "description": "AgentTranserRequest",
                "createdAt": "2018-11-20T04:33:56.486Z",
                "modifiedAt": "2018-11-20T04:33:56.486Z"
            },
            {
                "name": "AgentTransfer",
                "description": "AgentTransfer",
                "createdAt": "2018-11-20T04:34:28.500Z",
                "modifiedAt": "2018-11-20T04:34:28.500Z"
            }
        ],
        "synonyms": [],
        "phrases": [
            {
                "phrase": [
                    "AL",
                    "BHM",
                    "DHN",
                    "HSV",
                    "MOB",
                    "MGM",
                    "AK",
                    "ANC",
                    "FAI",
                    "JNU",
                    "AZ",
                    "FLG",
                    "PHX",
                    "TUS",
                    "YUM",
                    "AR",
                    "FYV",
                    "LIT",
                    "CA",
                    "BUR",
                    "FAT",
                    "LGB",
                    "LAX",
                    "OAK",
                    "ONT",
                    "PSP",
                    "SMF",
                    "SAN",
                    "SFO",
                    "SJC",
                    "SNA",
                    "CO",
                    "ASE",
                    "COS",
                    "DEN",
                    "GJT",
                    "PUB",
                    "CT",
                    "BDL",
                    "DC",
                    "IAD",
                    "DCA",
                    "FL",
                    "DAB",
                    "FLL",
                    "RSW",
                    "JAX",
                    "EYW",
                    "MIA",
                    "MCO",
                    "PNS",
                    "PIE",
                    "SRQ",
                    "TPA",
                    "PBI",
                    "PFN",
                    "GA",
                    "ATL",
                    "AGS",
                    "SAV",
                    "HI01",
                    "ITO",
                    "HNL",
                    "OGG",
                    "KOA",
                    "LIH",
                    "ID",
                    "BOI",
                    "IL",
                    "MDW",
                    "ORD",
                    "MLI",
                    "PIA",
                    "EVV",
                    "FWA",
                    "IND",
                    "SBN",
                    "IA",
                    "CID",
                    "DSM",
                    "KS",
                    "ICT",
                    "KY",
                    "LEX",
                    "SDF",
                    "LA",
                    "BTR",
                    "MSY",
                    "SHV",
                    "ME",
                    "AUG",
                    "BGR",
                    "PWM",
                    "MD",
                    "BWI",
                    "MA",
                    "BOS",
                    "HYA",
                    "ACK",
                    "ORH",
                    "MI",
                    "BTL",
                    "DTW",
                    "DET",
                    "FNT",
                    "GRR",
                    "AZO",
                    "LAN",
                    "MBS",
                    "MN",
                    "DLH",
                    "MSP",
                    "RST",
                    "MS",
                    "GPT",
                    "JAN",
                    "MO",
                    "MCI",
                    "STL",
                    "SGF",
                    "MT",
                    "BIL",
                    "NE",
                    "LNK",
                    "OMA",
                    "NV",
                    "LAS",
                    "RNO",
                    "NH",
                    "MHT",
                    "NJ",
                    "ACY",
                    "EWR",
                    "TTN",
                    "NM",
                    "ABQ",
                    "ALM",
                    "NY",
                    "ALB",
                    "BUF",
                    "ISP",
                    "JFK",
                    "LGA",
                    "SWF",
                    "ROC",
                    "SYR",
                    "HPN",
                    "NC",
                    "AVL",
                    "CLT",
                    "FAY",
                    "GSO",
                    "RDU",
                    "INT",
                    "ND",
                    "BIS",
                    "FAR",
                    "OH",
                    "CAK",
                    "CVG",
                    "CLE",
                    "CMH",
                    "DAY",
                    "TOL",
                    "OKC",
                    "TUL",
                    "OR",
                    "EUG",
                    "PDX",
                    "HIO",
                    "SLE",
                    "PA",
                    "ABE",
                    "ERI",
                    "MDT",
                    "PHL",
                    "PIT",
                    "AVP",
                    "RI",
                    "PVD",
                    "SC",
                    "CHS",
                    "CAE",
                    "GSP",
                    "MYR",
                    "SD",
                    "PIR",
                    "RAP",
                    "FSD",
                    "TN",
                    "TRI",
                    "CHA",
                    "TYS",
                    "MEM",
                    "BNA",
                    "TX",
                    "AMA",
                    "AUS",
                    "CRP",
                    "DAL",
                    "DFW",
                    "ELP",
                    "HOU",
                    "IAH",
                    "LBB",
                    "MAF",
                    "SAT",
                    "UT",
                    "SLC",
                    "VT",
                    "BTV",
                    "MPV",
                    "RUT",
                    "VA",
                    "IAD",
                    "PHF",
                    "ORF",
                    "RIC",
                    "ROA",
                    "WA",
                    "PSC",
                    "SEA",
                    "GEG",
                    "WV",
                    "CRW",
                    "CKB",
                    "WI",
                    "GRB",
                    "MSN",
                    "MKE",
                    "WY",
                    "CPR",
                    "CYS",
                    "JAC",
                    "RKS"
                ],
                "entity": "airport"
            },
            {
                "phrase": [
                    "US1423",
                    "AA1234",
                    "AA0172",
                    "SP1000",
                    "DL2001",
                    "SW1414",
                    "AL9898",
                    "FR4331"
                ],
                "entity": "flightno"
            },
            {
                "phrase": [
                    "Flight",
                    "air plane",
                    "aeroplane"
                ],
                "entity": "airtypes"
            },
            {
                "phrase": [
                    "abc",
                    "def"
                ],
                "entity": "test2"
            }
        ],
        "predefined_entities": [],
        "id": "RGF0YXNvdXJjZTo1ZDA3NTJlZjMwOGFhZTZhMTE5YWU0Mjc="
    },
    "projectId": "5d0752ee308aae6a119ae425",
    "userId": "58b79a695c280914dc30554b"
}

JSON Response:
{
    "data": {
        "updateDatasource": {
            "changedDatasource": {
                "_id": "5d0752ef308aae6a119ae427",
                "serviceid": "0AoI5SB5ILHozOHzl8f5wS5skmejKfp9GcTVayQiYFsCldHPJA1qD4RleUBJfga5",
                "utterances": [
                    {
                        "utterance": "qqqq",
                        "case_converted_utterance": "Qqqq",
                        "mapping": "{\"tokens\":[\"Qqqq\"],\"tags\":[{\"start\":0,\"tag\":\"sample\",\"end\":1,\"entity\":\"qqqq\"}],\"intent\":\"Weather\"}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "heyyy",
                        "case_converted_utterance": "Heyyy",
                        "mapping": "{\"tokens\":[\"Heyyy\"],\"tags\":[{\"start\":0,\"tag\":\"sample\",\"end\":1,\"entity\":\"heyyy\"}],\"intent\":\"test1\"}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "I want to do a travel",
                        "case_converted_utterance": "I want to do a travel",
                        "mapping": "{\"tokens\": [\"I\", \"want\", \"to\", \"do\", \"a\", \"travel\"], \"intent\": \"travelbooking\", \"tags\": [{\"start\": 5, \"tag\": \"TYPE\", \"end\": 6, \"score\": 0.5640399006298088, \"entity\": \"travel\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "travel booking",
                        "case_converted_utterance": "Travel booking",
                        "mapping": "{\"tokens\": [\"Travel\", \"booking\"], \"intent\": \"travelbooking\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.5286114190311912, \"entity\": \"travel\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "travel",
                        "case_converted_utterance": "Travel",
                        "mapping": "{\"tokens\": [\"Travel\"], \"intent\": \"travelbooking\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.2537922087668458, \"entity\": \"travel\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Please to a flight booking",
                        "case_converted_utterance": "Please to a flight booking",
                        "mapping": "{\"tokens\": [\"Please\", \"to\", \"a\", \"flight\", \"booking\"], \"intent\": \"airlinesearch\", \"tags\": [{\"start\": 3, \"tag\": \"mode\", \"end\": 4, \"entity\": \"flight\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "I would like to travel by flight",
                        "case_converted_utterance": "I would like to travel by flight",
                        "mapping": "{\"tokens\": [\"I\", \"would\", \"like\", \"to\", \"travel\", \"by\", \"flight\"], \"intent\": \"airlinesearch\", \"tags\": [{\"start\": 4, \"tag\": \"TYPE\", \"end\": 5, \"score\": 0.4979866350219423, \"entity\": \"travel\"}, {\"start\": 6, \"tag\": \"mode\", \"end\": 7, \"entity\": \"flight\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "kindly book one flight",
                        "case_converted_utterance": "Kindly book one flight",
                        "mapping": "{\"tokens\": [\"Kindly\", \"book\", \"one\", \"flight\"], \"intent\": \"airlinesearch\", \"tags\": [{\"start\": 3, \"tag\": \"mode\", \"end\": 4, \"entity\": \"flight\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "flight",
                        "case_converted_utterance": "Flight",
                        "mapping": "{\"tokens\": [\"Flight\"], \"intent\": \"airlinesearch\", \"tags\": [{\"start\": 0, \"tag\": \"mode\", \"end\": 1, \"entity\": \"flight\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Please book a flight ticket for me",
                        "case_converted_utterance": "Please book a flight ticket for me",
                        "mapping": "{\"tokens\": [\"Please\", \"book\", \"a\", \"flight\", \"ticket\", \"for\", \"me\"], \"intent\": \"airlinesearch\", \"tags\": [{\"start\": 0, \"tag\": \"mode\", \"end\": 1, \"entity\": \"\"}, {\"start\": 3, \"tag\": \"mode\", \"end\": 4, \"entity\": \"flight\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Please do a travel booking",
                        "case_converted_utterance": "Please do a travel booking",
                        "mapping": "{\"tokens\": [\"Please\", \"do\", \"a\", \"travel\", \"booking\"], \"intent\": \"travelbooking\", \"tags\": [{\"start\": 3, \"tag\": \"TYPE\", \"end\": 4, \"score\": 0.6740128800829303, \"entity\": \"travel\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "I want to travel",
                        "case_converted_utterance": "I want to travel",
                        "mapping": "{\"tokens\": [\"I\", \"want\", \"to\", \"travel\"], \"intent\": \"travelbooking\", \"tags\": [{\"start\": 3, \"tag\": \"TYPE\", \"end\": 4, \"score\": 0.3422346315669714, \"entity\": \"travel\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "I want travel",
                        "case_converted_utterance": "I want travel",
                        "mapping": "{\"tokens\": [\"I\", \"want\", \"travel\"], \"intent\": \"travelbooking\", \"tags\": [{\"start\": 2, \"tag\": \"TYPE\", \"end\": 3, \"score\": 0.23075157859533177, \"entity\": \"travel\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "I want to do booking",
                        "case_converted_utterance": "I want to do booking",
                        "mapping": "{\"tokens\": [\"I\", \"want\", \"to\", \"do\", \"booking\"], \"intent\": \"booking\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Please do a booking",
                        "case_converted_utterance": "Please do a booking",
                        "mapping": "{\"tokens\": [\"Please\", \"do\", \"a\", \"booking\"], \"intent\": \"booking\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Please booking",
                        "case_converted_utterance": "Please booking",
                        "mapping": "{\"tokens\": [\"Please\", \"booking\"], \"intent\": \"booking\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "I want to do a booking",
                        "case_converted_utterance": "I want to do a booking",
                        "mapping": "{\"tokens\": [\"I\", \"want\", \"to\", \"do\", \"a\", \"booking\"], \"intent\": \"booking\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "hiiii",
                        "case_converted_utterance": "Hiiii",
                        "mapping": "{\"tokens\": [\"Hiiii\"], \"intent\": \"Greeting\", \"tags\": [{\"start\": 0, \"tag\": \"MODE\", \"end\": 1, \"score\": 0.1243794318755859, \"entity\": \"hiiii\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "hi",
                        "case_converted_utterance": "Hi",
                        "mapping": "{\"tokens\": [\"Hi\"], \"intent\": \"Greeting\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "heyya",
                        "case_converted_utterance": "Heyya",
                        "mapping": "{\"tokens\": [\"Heyya\"], \"intent\": \"Greeting\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "hello",
                        "case_converted_utterance": "Hello",
                        "mapping": "{\"tokens\": [\"Hello\"], \"intent\": \"Greeting\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "hi",
                        "case_converted_utterance": "Hi",
                        "mapping": "{\"tokens\": [\"Hi\"], \"intent\": \"Greeting\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "You there",
                        "case_converted_utterance": "You there",
                        "mapping": "{\"tokens\": [\"You\", \"there\"], \"intent\": \"Greeting\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Hey",
                        "case_converted_utterance": "Hey",
                        "mapping": "{\"tokens\": [\"Hey\"], \"intent\": \"Greeting\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Hai",
                        "case_converted_utterance": "Hai",
                        "mapping": "{\"tokens\": [\"Hai\"], \"intent\": \"Greeting\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Hi",
                        "case_converted_utterance": "Hi",
                        "mapping": "{\"tokens\": [\"Hi\"], \"intent\": \"Greeting\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Good morning",
                        "case_converted_utterance": "Good morning",
                        "mapping": "{\"tokens\": [\"Good\", \"morning\"], \"intent\": \"Greeting\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.2530555062914658, \"entity\": \"Good\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Good day",
                        "case_converted_utterance": "Good day",
                        "mapping": "{\"tokens\": [\"Good\", \"day\"], \"intent\": \"Greeting\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.2684357011642687, \"entity\": \"Good\"}, {\"start\": 1, \"tag\": \"airport\", \"end\": 2, \"entity\": \"day\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Good evening",
                        "case_converted_utterance": "Good evening",
                        "mapping": "{\"tokens\": [\"Good\", \"evening\"], \"intent\": \"Greeting\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Hey twin",
                        "case_converted_utterance": "Hey twin",
                        "mapping": "{\"tokens\": [\"Hey\", \"twin\"], \"intent\": \"Greeting\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Hi there",
                        "case_converted_utterance": "Hi there",
                        "mapping": "{\"tokens\": [\"Hi\", \"there\"], \"intent\": \"Greeting\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "What'S up ?",
                        "case_converted_utterance": "What'S up ?",
                        "mapping": "{\"tokens\": [\"What'S\", \"up\", \"?\"], \"intent\": \"Greeting\", \"tags\": [{\"start\": 2, \"tag\": \"MODE\", \"end\": 3, \"score\": 0.3594824179203809, \"entity\": \"?\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Who is this ?",
                        "case_converted_utterance": "Who is this ?",
                        "mapping": "{\"tokens\": [\"Who\", \"is\", \"this\", \"?\"], \"intent\": \"Greeting\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "What'S new ?",
                        "case_converted_utterance": "What'S new ?",
                        "mapping": "{\"tokens\": [\"What'S\", \"new\", \"?\"], \"intent\": \"Greeting\", \"tags\": [{\"start\": 0, \"tag\": \"MODE\", \"end\": 1, \"score\": 0.276929868992718, \"entity\": \"What'S\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Hey there",
                        "case_converted_utterance": "Hey there",
                        "mapping": "{\"tokens\": [\"Hey\", \"there\"], \"intent\": \"Greeting\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Ok take me back",
                        "case_converted_utterance": "Ok take me back",
                        "mapping": "{\"tokens\": [\"Ok\", \"take\", \"me\", \"back\"], \"intent\": \"Greeting\", \"tags\": [{\"start\": 2, \"tag\": \"airport\", \"end\": 3, \"entity\": \"me\"}, {\"start\": 3, \"tag\": \"MODE\", \"end\": 4, \"score\": 0.28095878767074006, \"entity\": \"back\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Looking good eve",
                        "case_converted_utterance": "Looking good eve",
                        "mapping": "{\"tokens\": [\"Looking\", \"good\", \"eve\"], \"intent\": \"Greeting\", \"tags\": [{\"start\": 2, \"tag\": \"MODE\", \"end\": 3, \"score\": 0.3454258060185423, \"entity\": \"eve\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "How R U ?",
                        "case_converted_utterance": "How R U ?",
                        "mapping": "{\"tokens\": [\"How\", \"R\", \"U\", \"?\"], \"intent\": \"Greeting\", \"tags\": [{\"start\": 0, \"tag\": \"sample\", \"end\": 4, \"entity\": \"How R U ?\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "How is it going ?",
                        "case_converted_utterance": "How is it going ?",
                        "mapping": "{\"tokens\": [\"How\", \"is\", \"it\", \"going\", \"?\"], \"intent\": \"Greeting\", \"tags\": [{\"start\": 4, \"tag\": \"MODE\", \"end\": 5, \"score\": 0.22077778757291347, \"entity\": \"?\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "How have you been ?",
                        "case_converted_utterance": "How have you been ?",
                        "mapping": "{\"tokens\": [\"How\", \"have\", \"you\", \"been\", \"?\"], \"intent\": \"Greeting\", \"tags\": [{\"start\": 4, \"tag\": \"MODE\", \"end\": 5, \"score\": 0.21941104933103223, \"entity\": \"?\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "How are you today ?",
                        "case_converted_utterance": "How are you today ?",
                        "mapping": "{\"tokens\": [\"How\", \"are\", \"you\", \"today\", \"?\"], \"intent\": \"Greeting\", \"tags\": [{\"start\": 4, \"tag\": \"MODE\", \"end\": 5, \"score\": 0.22229289284995607, \"entity\": \"?\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "How are things going ?",
                        "case_converted_utterance": "How are things going ?",
                        "mapping": "{\"tokens\": [\"How\", \"are\", \"things\", \"going\", \"?\"], \"intent\": \"Greeting\", \"tags\": [{\"start\": 4, \"tag\": \"MODE\", \"end\": 5, \"score\": 0.22077778757291347, \"entity\": \"?\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Hello I am looking for some help here",
                        "case_converted_utterance": "Hello I am looking for some help here",
                        "mapping": "{\"tokens\": [\"Hello\", \"I\", \"am\", \"looking\", \"for\", \"some\", \"help\", \"here\"], \"intent\": \"Greeting\", \"tags\": [{\"start\": 0, \"tag\": \"sample\", \"end\": 3, \"entity\": \"Hello I am\"}, {\"start\": 6, \"tag\": \"TYPE\", \"end\": 7, \"score\": 0.11152091750581689, \"entity\": \"help\"}, {\"start\": 7, \"tag\": \"MODE\", \"end\": 8, \"score\": 0.21238762326047897, \"entity\": \"here\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Hi advisor",
                        "case_converted_utterance": "Hi advisor",
                        "mapping": "{\"tokens\": [\"Hi\", \"advisor\"], \"intent\": \"Greeting\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Hey you",
                        "case_converted_utterance": "Hey you",
                        "mapping": "{\"tokens\": [\"Hey\", \"you\"], \"intent\": \"Greeting\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Hey there all",
                        "case_converted_utterance": "Hey there all",
                        "mapping": "{\"tokens\": [\"Hey\", \"there\", \"all\"], \"intent\": \"Greeting\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Hey how are you doing",
                        "case_converted_utterance": "Hey how are you doing",
                        "mapping": "{\"tokens\": [\"Hey\", \"how\", \"are\", \"you\", \"doing\"], \"intent\": \"Greeting\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Hello",
                        "case_converted_utterance": "Hello",
                        "mapping": "{\"tokens\": [\"Hello\"], \"intent\": \"Greeting\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Hello agent",
                        "case_converted_utterance": "Hello agent",
                        "mapping": "{\"tokens\": [\"Hello\", \"agent\"], \"intent\": \"Greeting\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Have you been well ?",
                        "case_converted_utterance": "Have you been well ?",
                        "mapping": "{\"tokens\": [\"Have\", \"you\", \"been\", \"well\", \"?\"], \"intent\": \"Greeting\", \"tags\": [{\"start\": 2, \"tag\": \"MODE\", \"end\": 3, \"score\": 0.2390684494907248, \"entity\": \"been\"}, {\"start\": 4, \"tag\": \"MODE\", \"end\": 5, \"score\": 0.2158975453646159, \"entity\": \"?\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Greetings",
                        "case_converted_utterance": "Greetings",
                        "mapping": "{\"tokens\": [\"Greetings\"], \"intent\": \"Greeting\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Good to see you",
                        "case_converted_utterance": "Good to see you",
                        "mapping": "{\"tokens\": [\"Good\", \"to\", \"see\", \"you\"], \"intent\": \"Greeting\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "no",
                        "case_converted_utterance": "No",
                        "mapping": "{\"tokens\": [\"No\"], \"intent\": \"conclusionflow\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "no thank you",
                        "case_converted_utterance": "No thank you",
                        "mapping": "{\"tokens\": [\"No\", \"thank\", \"you\"], \"intent\": \"conclusionflow\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "hello",
                        "case_converted_utterance": "Hello",
                        "mapping": "{\"tokens\": [\"Hello\"], \"intent\": \"test1\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "23394 weather",
                        "case_converted_utterance": "23394 weather",
                        "mapping": "{\"tokens\": [\"23394\", \"weather\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"sample\", \"end\": 2, \"entity\": \"23394 weather\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Weather of 23294",
                        "case_converted_utterance": "Weather of 23294",
                        "mapping": "{\"tokens\": [\"Weather\", \"of\", \"23294\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.1381967649210164, \"entity\": \"Weather\"}, {\"start\": 1, \"tag\": \"sample\", \"end\": 3, \"entity\": \"of 23294\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Temperature of 695024",
                        "case_converted_utterance": "Temperature of 695024",
                        "mapping": "{\"tokens\": [\"Temperature\", \"of\", \"695024\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.11583915744592144, \"entity\": \"Temperature\"}, {\"start\": 1, \"tag\": \"sample\", \"end\": 3, \"entity\": \"of 695024\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Temperature of Manchester",
                        "case_converted_utterance": "Temperature of Manchester",
                        "mapping": "{\"tokens\": [\"Temperature\", \"of\", \"Manchester\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.11583915744592144, \"entity\": \"Temperature\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Weather of La",
                        "case_converted_utterance": "Weather of La",
                        "mapping": "{\"tokens\": [\"Weather\", \"of\", \"La\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.1381967649210164, \"entity\": \"Weather\"}, {\"start\": 2, \"tag\": \"airport\", \"end\": 3, \"entity\": \"La\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Zzzz 0Zz weather",
                        "case_converted_utterance": "Zzzz 0Zz weather",
                        "mapping": "{\"tokens\": [\"Zzzz\", \"0Zz\", \"weather\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"sample\", \"end\": 2, \"entity\": \"Zzzz 0Zz\"}, {\"start\": 2, \"tag\": \"MODE\", \"end\": 3, \"score\": 0.10199896814355316, \"entity\": \"weather\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Weather of XXXX XXX",
                        "case_converted_utterance": "Weather of XXXX XXX",
                        "mapping": "{\"tokens\": [\"Weather\", \"of\", \"XXXX\", \"XXX\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.1381967649210164, \"entity\": \"Weather\"}, {\"start\": 1, \"tag\": \"sample\", \"end\": 4, \"entity\": \"of XXXX XXX\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "99900 weather",
                        "case_converted_utterance": "99900 weather",
                        "mapping": "{\"tokens\": [\"99900\", \"weather\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"sample\", \"end\": 2, \"entity\": \"99900 weather\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Trivandrum weather",
                        "case_converted_utterance": "Trivandrum weather",
                        "mapping": "{\"tokens\": [\"Trivandrum\", \"weather\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.10129349747641157, \"entity\": \"Trivandrum\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Weather of Trivandrum",
                        "case_converted_utterance": "Weather of Trivandrum",
                        "mapping": "{\"tokens\": [\"Weather\", \"of\", \"Trivandrum\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.1381967649210164, \"entity\": \"Weather\"}, {\"start\": 2, \"tag\": \"MODE\", \"end\": 3, \"score\": 0.12936659812427925, \"entity\": \"Trivandrum\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Temperature of Trivandrum",
                        "case_converted_utterance": "Temperature of Trivandrum",
                        "mapping": "{\"tokens\": [\"Temperature\", \"of\", \"Trivandrum\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.11583915744592144, \"entity\": \"Temperature\"}, {\"start\": 2, \"tag\": \"MODE\", \"end\": 3, \"score\": 0.12936659812427925, \"entity\": \"Trivandrum\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Climate of Trivandrum",
                        "case_converted_utterance": "Climate of Trivandrum",
                        "mapping": "{\"tokens\": [\"Climate\", \"of\", \"Trivandrum\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.109057259808529, \"entity\": \"Climate\"}, {\"start\": 2, \"tag\": \"MODE\", \"end\": 3, \"score\": 0.12936659812427925, \"entity\": \"Trivandrum\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Show me weather of Chennai",
                        "case_converted_utterance": "Show me weather of Chennai",
                        "mapping": "{\"tokens\": [\"Show\", \"me\", \"weather\", \"of\", \"Chennai\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"MODE\", \"end\": 1, \"score\": 0.14623363065090153, \"entity\": \"Show\"}, {\"start\": 1, \"tag\": \"airport\", \"end\": 2, \"entity\": \"me\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Show me weather",
                        "case_converted_utterance": "Show me weather",
                        "mapping": "{\"tokens\": [\"Show\", \"me\", \"weather\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"MODE\", \"end\": 1, \"score\": 0.14623363065090153, \"entity\": \"Show\"}, {\"start\": 1, \"tag\": \"airport\", \"end\": 2, \"entity\": \"me\"}, {\"start\": 2, \"tag\": \"MODE\", \"end\": 3, \"score\": 0.10241400032170002, \"entity\": \"weather\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Whats weather",
                        "case_converted_utterance": "Whats weather",
                        "mapping": "{\"tokens\": [\"Whats\", \"weather\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"MODE\", \"end\": 1, \"score\": 0.11176551876495047, \"entity\": \"Whats\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Weather of a place",
                        "case_converted_utterance": "Weather of a place",
                        "mapping": "{\"tokens\": [\"Weather\", \"of\", \"a\", \"place\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.1381967649210164, \"entity\": \"Weather\"}, {\"start\": 3, \"tag\": \"TYPE\", \"end\": 4, \"score\": 0.1408800672112676, \"entity\": \"place\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Weather of London",
                        "case_converted_utterance": "Weather of London",
                        "mapping": "{\"tokens\": [\"Weather\", \"of\", \"London\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.1381967649210164, \"entity\": \"Weather\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Cochin weather",
                        "case_converted_utterance": "Cochin weather",
                        "mapping": "{\"tokens\": [\"Cochin\", \"weather\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.12158444891058733, \"entity\": \"Cochin\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Weather forcast",
                        "case_converted_utterance": "Weather forcast",
                        "mapping": "{\"tokens\": [\"Weather\", \"forcast\"], \"text\": null, \"intent\": \"Weather\", \"tags\": [{\"start\": 0, \"tag\": \"TYPE\", \"end\": 1, \"score\": 0.13702922069323892, \"entity\": \"Weather\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "What is the whether now for",
                        "case_converted_utterance": "What is the whether now for",
                        "mapping": "{\"tokens\": [\"What\", \"is\", \"the\", \"whether\", \"now\", \"for\"], \"text\": null, \"intent\": \"Weather\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "test here",
                        "case_converted_utterance": "Test here",
                        "mapping": "{\"tokens\": [\"Test\", \"here\"], \"text\": null, \"intent\": \"test1\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "No thanks",
                        "case_converted_utterance": "No thanks",
                        "mapping": "{\"tokens\": [\"No\", \"thanks\"], \"text\": null, \"intent\": \"conclusionflow\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "i want to book a travel ticket",
                        "case_converted_utterance": "I want to book a travel ticket",
                        "mapping": "{\"tokens\": [\"I\", \"want\", \"to\", \"book\", \"a\", \"travel\", \"ticket\"], \"text\": null, \"intent\": \"travelbooking\", \"tags\": [{\"start\": 5, \"tag\": \"type\", \"end\": 6, \"entity\": \"travel\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Hello how are you ",
                        "case_converted_utterance": "Hello how are you ",
                        "mapping": "{\"tokens\": [\"Hello\", \"how\", \"are\", \"you\"], \"text\": null, \"intent\": \"greetings\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Hi how are you ",
                        "case_converted_utterance": "Hi how are you ",
                        "mapping": "{\"tokens\": [\"Hi\", \"how\", \"are\", \"you\"], \"text\": null, \"intent\": \"greetings\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Book a ticket for me ",
                        "case_converted_utterance": "Book a ticket for me ",
                        "mapping": "{\"tokens\": [\"Book\", \"a\", \"ticket\", \"for\", \"me\"], \"text\": null, \"intent\": \"booking\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Please book a ticket ",
                        "case_converted_utterance": "Please book a ticket ",
                        "mapping": "{\"tokens\": [\"Please\", \"book\", \"a\", \"ticket\"], \"text\": null, \"intent\": \"booking\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Hello there ",
                        "case_converted_utterance": "Hello there ",
                        "mapping": "{\"tokens\": [\"Hello\", \"there\"], \"text\": null, \"intent\": \"greetings\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Hello ",
                        "case_converted_utterance": "Hello ",
                        "mapping": "{\"tokens\": [\"Hello\"], \"text\": null, \"intent\": \"greetings\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Anybody there ",
                        "case_converted_utterance": "Anybody there ",
                        "mapping": "{\"tokens\": [\"Anybody\", \"there\"], \"text\": null, \"intent\": \"greetings\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Hi there ",
                        "case_converted_utterance": "Hi there ",
                        "mapping": "{\"tokens\": [\"Hi\", \"there\"], \"text\": null, \"intent\": \"greetings\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Hi ",
                        "case_converted_utterance": "Hi ",
                        "mapping": "{\"tokens\": [\"Hi\"], \"text\": null, \"intent\": \"greetings\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Movie ",
                        "case_converted_utterance": "Movie ",
                        "mapping": "{\"tokens\": [\"Movie\"], \"text\": null, \"intent\": \"moviebooking\", \"tags\": [{\"start\": 0, \"tag\": \"type\", \"end\": 1, \"entity\": \"Movie\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Please make a movie booking ",
                        "case_converted_utterance": "Please make a movie booking ",
                        "mapping": "{\"tokens\": [\"Please\", \"make\", \"a\", \"movie\", \"booking\"], \"text\": null, \"intent\": \"moviebooking\", \"tags\": [{\"start\": 3, \"tag\": \"type\", \"end\": 4, \"entity\": \"movie\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "No please ",
                        "case_converted_utterance": "No please ",
                        "mapping": "{\"tokens\": [\"No\", \"please\"], \"text\": null, \"intent\": \"conclusion\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Good thanks ",
                        "case_converted_utterance": "Good thanks ",
                        "mapping": "{\"tokens\": [\"Good\", \"thanks\"], \"text\": null, \"intent\": \"conclusion\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Thanks I am good ",
                        "case_converted_utterance": "Thanks I am good ",
                        "mapping": "{\"tokens\": [\"Thanks\", \"I\", \"am\", \"good\"], \"text\": null, \"intent\": \"conclusion\", \"tags\": [{\"start\": 0, \"tag\": \"sample\", \"end\": 3, \"entity\": \"Thanks I am\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "No thanks ",
                        "case_converted_utterance": "No thanks ",
                        "mapping": "{\"tokens\": [\"No\", \"thanks\"], \"text\": null, \"intent\": \"conclusion\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Go ahead ",
                        "case_converted_utterance": "Go ahead ",
                        "mapping": "{\"tokens\": [\"Go\", \"ahead\"], \"text\": null, \"intent\": \"successflow\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Yes ",
                        "case_converted_utterance": "Yes ",
                        "mapping": "{\"tokens\": [\"Yes\"], \"text\": null, \"intent\": \"successflow\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Sure ",
                        "case_converted_utterance": "Sure ",
                        "mapping": "{\"tokens\": [\"Sure\"], \"text\": null, \"intent\": \"successflow\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Ok sure ",
                        "case_converted_utterance": "Ok sure ",
                        "mapping": "{\"tokens\": [\"Ok\", \"sure\"], \"text\": null, \"intent\": \"successflow\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Please go ahead ",
                        "case_converted_utterance": "Please go ahead ",
                        "mapping": "{\"tokens\": [\"Please\", \"go\", \"ahead\"], \"text\": null, \"intent\": \"successflow\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Yes please ",
                        "case_converted_utterance": "Yes please ",
                        "mapping": "{\"tokens\": [\"Yes\", \"please\"], \"text\": null, \"intent\": \"successflow\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Please do a travel booking ",
                        "case_converted_utterance": "Please do a travel booking ",
                        "mapping": "{\"tokens\": [\"Please\", \"do\", \"a\", \"travel\", \"booking\"], \"text\": null, \"intent\": \"travelbooking\", \"tags\": [{\"start\": 3, \"tag\": \"type\", \"end\": 4, \"entity\": \"travel\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Please do a booking ",
                        "case_converted_utterance": "Please do a booking ",
                        "mapping": "{\"tokens\": [\"Please\", \"do\", \"a\", \"booking\"], \"text\": null, \"intent\": \"booking\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "I want to make a travel booking ",
                        "case_converted_utterance": "I want to make a travel booking ",
                        "mapping": "{\"tokens\": [\"I\", \"want\", \"to\", \"make\", \"a\", \"travel\", \"booking\"], \"text\": null, \"intent\": \"travelbooking\", \"tags\": [{\"start\": 5, \"tag\": \"type\", \"end\": 6, \"entity\": \"travel\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "Please help in booking a travel ",
                        "case_converted_utterance": "Please help in booking a travel ",
                        "mapping": "{\"tokens\": [\"Please\", \"help\", \"in\", \"booking\", \"a\", \"travel\"], \"text\": null, \"intent\": \"travelbooking\", \"tags\": [{\"start\": 5, \"tag\": \"type\", \"end\": 6, \"entity\": \"travel\"}]}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "I want to make a booking ",
                        "case_converted_utterance": "I want to make a booking ",
                        "mapping": "{\"tokens\": [\"I\", \"want\", \"to\", \"make\", \"a\", \"booking\"], \"text\": null, \"intent\": \"booking\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    },
                    {
                        "utterance": "I would like to make a booking ",
                        "case_converted_utterance": "I would like to make a booking ",
                        "mapping": "{\"tokens\": [\"I\", \"would\", \"like\", \"to\", \"make\", \"a\", \"booking\"], \"text\": null, \"intent\": \"booking\", \"tags\": []}",
                        "ir_trained": false,
                        "ner_trained": false
                    }
                ],
                "entities": [
                    "type",
                    "mode",
                    "travelcount",
                    "bagsize",
                    "SAMPLE1"
                ],
                "intents": [
                    {
                        "name": "No intent",
                        "description": "Add the utterances that should not be labelled as any of your intents here.",
                        "createdAt": "2019-06-17T08:44:31.450Z",
                        "modifiedAt": "2019-06-17T08:44:31.450Z"
                    },
                    {
                        "name": "Greeting",
                        "description": "Marks the beginning of a conversation",
                        "createdAt": "2018-11-20T05:37:51.070Z",
                        "modifiedAt": "2018-11-20T05:37:51.070Z"
                    },
                    {
                        "name": "Weather",
                        "description": "Indicates that the user wants to know about the weather",
                        "createdAt": "2018-11-01T09:10:42.935Z",
                        "modifiedAt": "2018-11-01T09:10:42.935Z"
                    },
                    {
                        "name": "test1",
                        "description": "test",
                        "createdAt": "2018-11-01T09:10:08.712Z",
                        "modifiedAt": "2018-11-01T09:10:08.712Z"
                    },
                    {
                        "name": "booking",
                        "description": "booking",
                        "createdAt": "2018-11-01T08:44:06.846Z",
                        "modifiedAt": "2018-11-01T08:44:06.846Z"
                    },
                    {
                        "name": "travelbooking",
                        "description": "travelbooking",
                        "createdAt": "2018-10-25T09:21:34.482Z",
                        "modifiedAt": "2018-10-25T09:21:34.482Z"
                    },
                    {
                        "name": "greetings",
                        "description": "greetings",
                        "createdAt": "2018-10-25T09:21:34.482Z",
                        "modifiedAt": "2018-10-25T09:21:34.482Z"
                    },
                    {
                        "name": "conclusion",
                        "description": "conclusion",
                        "createdAt": "2018-10-25T09:21:34.482Z",
                        "modifiedAt": "2018-10-25T09:21:34.482Z"
                    },
                    {
                        "name": "successflow",
                        "description": "successflow",
                        "createdAt": "2018-10-25T09:21:34.482Z",
                        "modifiedAt": "2018-10-25T09:21:34.482Z"
                    },
                    {
                        "name": "moviebooking",
                        "description": "moviebooking",
                        "createdAt": "2018-10-25T09:21:34.482Z",
                        "modifiedAt": "2018-10-25T09:21:34.482Z"
                    },
                    {
                        "name": "airlinesearch",
                        "description": "airlinesearch",
                        "createdAt": "2018-10-25T09:21:34.482Z",
                        "modifiedAt": "2018-10-25T09:21:34.482Z"
                    },
                    {
                        "name": "airlinebooking",
                        "description": "airlinebooking",
                        "createdAt": "2018-10-25T09:21:34.482Z",
                        "modifiedAt": "2018-10-25T09:21:34.482Z"
                    },
                    {
                        "name": "conclusionflow",
                        "description": "conclusionflow",
                        "createdAt": "2018-10-25T09:21:34.482Z",
                        "modifiedAt": "2018-10-25T09:21:34.482Z"
                    },
                    {
                        "name": "AgentTranserRequest",
                        "description": "AgentTranserRequest",
                        "createdAt": "2018-11-20T04:33:56.486Z",
                        "modifiedAt": "2018-11-20T04:33:56.486Z"
                    },
                    {
                        "name": "AgentTransfer",
                        "description": "AgentTransfer",
                        "createdAt": "2018-11-20T04:34:28.500Z",
                        "modifiedAt": "2018-11-20T04:34:28.500Z"
                    }
                ],
                "trainEntity": true,
                "trainIntent": true,
                "predefined_entities": [],
                "patterns": [
                    {
                        "pattern": "\\d{4}\\s/\\s\\d{2}\\s/\\s\\d{2}|\\d{2}\\s/\\s\\d{2}\\s/\\s\\d{4}",
                        "entity": "CUSTOM_DATE"
                    },
                    {
                        "pattern": "[0-9A-Z, ]{3,6}",
                        "entity": "sample"
                    },
                    {
                        "pattern": "[a-z0-9A-Z_.-]+@[da-zA-Z.-]+.[a-zA-Z.]{2,6}",
                        "entity": "email"
                    }
                ],
                "phrases": [
                    {
                        "phrase": [
                            "AL",
                            "BHM",
                            "DHN",
                            "HSV",
                            "MOB",
                            "MGM",
                            "AK",
                            "ANC",
                            "FAI",
                            "JNU",
                            "AZ",
                            "FLG",
                            "PHX",
                            "TUS",
                            "YUM",
                            "AR",
                            "FYV",
                            "LIT",
                            "CA",
                            "BUR",
                            "FAT",
                            "LGB",
                            "LAX",
                            "OAK",
                            "ONT",
                            "PSP",
                            "SMF",
                            "SAN",
                            "SFO",
                            "SJC",
                            "SNA",
                            "CO",
                            "ASE",
                            "COS",
                            "DEN",
                            "GJT",
                            "PUB",
                            "CT",
                            "BDL",
                            "DC",
                            "IAD",
                            "DCA",
                            "FL",
                            "DAB",
                            "FLL",
                            "RSW",
                            "JAX",
                            "EYW",
                            "MIA",
                            "MCO",
                            "PNS",
                            "PIE",
                            "SRQ",
                            "TPA",
                            "PBI",
                            "PFN",
                            "GA",
                            "ATL",
                            "AGS",
                            "SAV",
                            "HI01",
                            "ITO",
                            "HNL",
                            "OGG",
                            "KOA",
                            "LIH",
                            "ID",
                            "BOI",
                            "IL",
                            "MDW",
                            "ORD",
                            "MLI",
                            "PIA",
                            "EVV",
                            "FWA",
                            "IND",
                            "SBN",
                            "IA",
                            "CID",
                            "DSM",
                            "KS",
                            "ICT",
                            "KY",
                            "LEX",
                            "SDF",
                            "LA",
                            "BTR",
                            "MSY",
                            "SHV",
                            "ME",
                            "AUG",
                            "BGR",
                            "PWM",
                            "MD",
                            "BWI",
                            "MA",
                            "BOS",
                            "HYA",
                            "ACK",
                            "ORH",
                            "MI",
                            "BTL",
                            "DTW",
                            "DET",
                            "FNT",
                            "GRR",
                            "AZO",
                            "LAN",
                            "MBS",
                            "MN",
                            "DLH",
                            "MSP",
                            "RST",
                            "MS",
                            "GPT",
                            "JAN",
                            "MO",
                            "MCI",
                            "STL",
                            "SGF",
                            "MT",
                            "BIL",
                            "NE",
                            "LNK",
                            "OMA",
                            "NV",
                            "LAS",
                            "RNO",
                            "NH",
                            "MHT",
                            "NJ",
                            "ACY",
                            "EWR",
                            "TTN",
                            "NM",
                            "ABQ",
                            "ALM",
                            "NY",
                            "ALB",
                            "BUF",
                            "ISP",
                            "JFK",
                            "LGA",
                            "SWF",
                            "ROC",
                            "SYR",
                            "HPN",
                            "NC",
                            "AVL",
                            "CLT",
                            "FAY",
                            "GSO",
                            "RDU",
                            "INT",
                            "ND",
                            "BIS",
                            "FAR",
                            "OH",
                            "CAK",
                            "CVG",
                            "CLE",
                            "CMH",
                            "DAY",
                            "TOL",
                            "OKC",
                            "TUL",
                            "OR",
                            "EUG",
                            "PDX",
                            "HIO",
                            "SLE",
                            "PA",
                            "ABE",
                            "ERI",
                            "MDT",
                            "PHL",
                            "PIT",
                            "AVP",
                            "RI",
                            "PVD",
                            "SC",
                            "CHS",
                            "CAE",
                            "GSP",
                            "MYR",
                            "SD",
                            "PIR",
                            "RAP",
                            "FSD",
                            "TN",
                            "TRI",
                            "CHA",
                            "TYS",
                            "MEM",
                            "BNA",
                            "TX",
                            "AMA",
                            "AUS",
                            "CRP",
                            "DAL",
                            "DFW",
                            "ELP",
                            "HOU",
                            "IAH",
                            "LBB",
                            "MAF",
                            "SAT",
                            "UT",
                            "SLC",
                            "VT",
                            "BTV",
                            "MPV",
                            "RUT",
                            "VA",
                            "IAD",
                            "PHF",
                            "ORF",
                            "RIC",
                            "ROA",
                            "WA",
                            "PSC",
                            "SEA",
                            "GEG",
                            "WV",
                            "CRW",
                            "CKB",
                            "WI",
                            "GRB",
                            "MSN",
                            "MKE",
                            "WY",
                            "CPR",
                            "CYS",
                            "JAC",
                            "RKS"
                        ],
                        "entity": "airport"
                    },
                    {
                        "phrase": [
                            "US1423",
                            "AA1234",
                            "AA0172",
                            "SP1000",
                            "DL2001",
                            "SW1414",
                            "AL9898",
                            "FR4331"
                        ],
                        "entity": "flightno"
                    },
                    {
                        "phrase": [
                            "Flight",
                            "air plane",
                            "aeroplane"
                        ],
                        "entity": "airtypes"
                    },
                    {
                        "phrase": [
                            "abc",
                            "def"
                        ],
                        "entity": "test2"
                    }
                ],
                "synonyms": []
            }
        }
    }
}

#####################################################################################################################
Fetch Projects:

Query:
const fetchProjectsQuery = `
query FetchProjects(
  $createdBy: ID,
  $name: String,
  $visibility:String)
  {
    getProjects(
      createdBy: $createdBy,
      name: $name,
      visibility:$visibility
    )
    {
      _id
      id
      name
      desc
      ner{
        status
        status_message
      }
      ir{
        status
        status_message
      }
      visibility
      createdBy {
        username
      }
      updatedAt
    }
}
`;

Request URL:
http://ice-xd.southindia.cloudapp.azure.com:3001/

POST Data:
{
    "name": "demo",
    "visibility": "private",
    "createdBy": "58b79a695c280914dc30554b"
}
58b79a695c280914dc30554b is the user id.

JSON Response:
{
    "data": {
        "getProjects": [
            {
                "_id": "5cf645ed308aae6a118094eb",
                "id": "UHJvamVjdDo1Y2Y2NDVlZDMwOGFhZTZhMTE4MDk0ZWI=",
                "name": "masterbotdemo",
                "desc": "masterbotdemo test qa",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-06-04T10:45:08.896Z"
            },
            {
                "_id": "5cf89f5d308aae6a11815960",
                "id": "UHJvamVjdDo1Y2Y4OWY1ZDMwOGFhZTZhMTE4MTU5NjA=",
                "name": "testspanishdemo",
                "desc": "testspanishdemo",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-06-06T05:13:39.389Z"
            },
            {
                "_id": "5b4c6956c9a9b809e138e0b7",
                "id": "UHJvamVjdDo1YjRjNjk1NmM5YTliODA5ZTEzOGUwYjc=",
                "name": "demo-project",
                "desc": "demo purpose",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jul-18-2018 05:22:03."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2018-07-16T09:47:07.438Z"
            },
            {
                "_id": "5badfd7cfc5bf109622d96ea",
                "id": "UHJvamVjdDo1YmFkZmQ3Y2ZjNWJmMTA5NjIyZDk2ZWE=",
                "name": "MasterDemo",
                "desc": "testing master greeting",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Sep-28-2018 10:14:21."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2018-09-28T10:08:06.288Z"
            },
            {
                "_id": "5bfbc0c435df3a6bd5f39852",
                "id": "UHJvamVjdDo1YmZiYzBjNDM1ZGYzYTZiZDVmMzk4NTI=",
                "name": "MedicalAssistant-Demo",
                "desc": "Demo project",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2018-11-26T09:45:40.674Z"
            },
            {
                "_id": "5cd2d5b36e08183753795e67",
                "id": "UHJvamVjdDo1Y2QyZDViMzZlMDgxODM3NTM3OTVlNjc=",
                "name": "demo-ss",
                "desc": "for demotest",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-05-08T13:12:20.352Z"
            },
            {
                "_id": "5ceb8deb47cf4e727461fc1d",
                "id": "UHJvamVjdDo1Y2ViOGRlYjQ3Y2Y0ZTcyNzQ2MWZjMWQ=",
                "name": "test-clones-demo",
                "desc": "testing new ",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-05-27T07:12:46.894Z"
            },
            {
                "_id": "5cfa4d15308aae6a118818b4",
                "id": "UHJvamVjdDo1Y2ZhNGQxNTMwOGFhZTZhMTE4ODE4YjQ=",
                "name": "DemoE2E-Resetpassword",
                "desc": "DemoE2E-Reset password",
                "ner": {
                    "status": "validated",
                    "status_message": "Validation completed successfully."
                },
                "ir": {
                    "status": "validated",
                    "status_message": "Validation completed successfully."
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-06-07T11:40:06.205Z"
            }
        ]
    }
}

######################################################################################################################
Load projects of the user:

Query:
const loadProjectByUserQuery = `
query FetchProjectQuery($createdBy: ID!){
      UserProjects: getProjects(createdBy: $createdBy, visibility:"private"){
     ...projectFields
      },
      PublicProjects: getProjects(visibility:"public" ) {
     ...projectFields
      },
    }

    fragment projectFields on Project {
      _id
      id
      name
      desc
      ner{
        status
        status_message
      }
      ir{
        status
        status_message
      }
      visibility
      createdBy {
        username
      }
      updatedAt
    }
`;

Request URL:
http://ice-xd.southindia.cloudapp.azure.com:3001/

POST Data:
{"createdBy":"58b79a695c280914dc30554b"}
58b79a695c280914dc30554b is the user id.

JSON Response:
{
    "data": {
        "UserProjects": [
            {
                "_id": "5cf645ed308aae6a118094eb",
                "id": "UHJvamVjdDo1Y2Y2NDVlZDMwOGFhZTZhMTE4MDk0ZWI=",
                "name": "masterbotdemo",
                "desc": "masterbotdemo test qa",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-06-04T10:45:08.896Z"
            },
            {
                "_id": "5c6f91c46e081837537e687d",
                "id": "UHJvamVjdDo1YzZmOTFjNDZlMDgxODM3NTM3ZTY4N2Q=",
                "name": "testprod",
                "desc": "testprod",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-05-02T09:43:47.278Z"
            },
            {
                "_id": "5c6f941e6e081837537e8123",
                "id": "UHJvamVjdDo1YzZmOTQxZTZlMDgxODM3NTM3ZTgxMjM=",
                "name": "testprod2",
                "desc": "testprod2",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-02-22T06:18:15.008Z"
            },
            {
                "_id": "5c6f9dfb6e081837537ee544",
                "id": "UHJvamVjdDo1YzZmOWRmYjZlMDgxODM3NTM3ZWU1NDQ=",
                "name": "testprod3",
                "desc": "testprod3",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-02-22T08:19:05.219Z"
            },
            {
                "_id": "5c6fb0a96e081837537feca5",
                "id": "UHJvamVjdDo1YzZmYjBhOTZlMDgxODM3NTM3ZmVjYTU=",
                "name": "slavebot1",
                "desc": "slavebot1",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-02-22T08:19:56.348Z"
            },
            {
                "_id": "5c6fb13c6e081837538001e9",
                "id": "UHJvamVjdDo1YzZmYjEzYzZlMDgxODM3NTM4MDAxZTk=",
                "name": "masterbottest",
                "desc": "masterbottest",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-02-22T08:22:21.440Z"
            },
            {
                "_id": "5cef9c46308aae6a11715f92",
                "id": "UHJvamVjdDo1Y2VmOWM0NjMwOGFhZTZhMTE3MTVmOTI=",
                "name": "testNER",
                "desc": "TestDemo",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-05-30T10:57:21.708Z"
            },
            {
                "_id": "5cf89f5d308aae6a11815960",
                "id": "UHJvamVjdDo1Y2Y4OWY1ZDMwOGFhZTZhMTE4MTU5NjA=",
                "name": "testspanishdemo",
                "desc": "testspanishdemo",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-06-06T05:13:39.389Z"
            },
            {
                "_id": "5d0c6f49308aae6a11a64deb",
                "id": "UHJvamVjdDo1ZDBjNmY0OTMwOGFhZTZhMTFhNjRkZWI=",
                "name": "wefre",
                "desc": "frere",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-06-21T05:46:50.186Z"
            },
            {
                "_id": "5d120b26308aae6a11b91b6d",
                "id": "UHJvamVjdDo1ZDEyMGIyNjMwOGFhZTZhMTFiOTFiNmQ=",
                "name": "TestDelete2",
                "desc": "Delete test2",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-06-26T04:22:13.785Z"
            },
            {
                "_id": "5d132049144b351403261785",
                "id": "UHJvamVjdDo1ZDEzMjA0OTE0NGIzNTE0MDMyNjE3ODU=",
                "name": "qqqqq",
                "desc": "qqqqq",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-06-26T07:35:38.420Z"
            },
            {
                "_id": "5d1332bc144b35140326d649",
                "id": "UHJvamVjdDo1ZDEzMzJiYzE0NGIzNTE0MDMyNmQ2NDk=",
                "name": "TicketIntent",
                "desc": "Identify intent from ticket description",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-06-26T08:54:21.966Z"
            },
            {
                "_id": "5d133dd3144b351403286157",
                "id": "UHJvamVjdDo1ZDEzM2RkMzE0NGIzNTE0MDMyODYxNTc=",
                "name": "ConfirmResponses",
                "desc": "ConfirmResponses",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-06-26T09:41:40.281Z"
            },
            {
                "_id": "5d135b87144b3514032b27f9",
                "id": "UHJvamVjdDo1ZDEzNWI4NzE0NGIzNTE0MDMyYjI3Zjk=",
                "name": "qwerty",
                "desc": "qwerty111",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-06-26T11:56:23.776Z"
            },
            {
                "_id": "5cf4ca2c308aae6a11775254",
                "id": "UHJvamVjdDo1Y2Y0Y2EyYzMwOGFhZTZhMTE3NzUyNTQ=",
                "name": "testspanish1",
                "desc": "testspanish1",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-06-03T07:20:15.614Z"
            },
            {
                "_id": "5cf9eff6308aae6a1183b138",
                "id": "UHJvamVjdDo1Y2Y5ZWZmNjMwOGFhZTZhMTE4M2IxMzg=",
                "name": "MasterBOT-DesignerTest",
                "desc": "MasterBOT-DesignerTest",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-06-07T05:02:48.761Z"
            },
            {
                "_id": "5cfdf5d7308aae6a1189b205",
                "id": "UHJvamVjdDo1Y2ZkZjVkNzMwOGFhZTZhMTE4OWIyMDU=",
                "name": "Test-NER",
                "desc": "Test project for NER",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-06-10T06:16:56.629Z"
            },
            {
                "_id": "5cfe002a308aae6a118a437d",
                "id": "UHJvamVjdDo1Y2ZlMDAyYTMwOGFhZTZhMTE4YTQzN2Q=",
                "name": "TestNERJSON",
                "desc": "TestNERJSON",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-06-10T07:01:02.814Z"
            },
            {
                "_id": "5cfe01ab308aae6a118a8aca",
                "id": "UHJvamVjdDo1Y2ZlMDFhYjMwOGFhZTZhMTE4YThhY2E=",
                "name": "E2ESample",
                "desc": "Test Project",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-06-10T07:07:26.072Z"
            },
            {
                "_id": "5b0544c50e8e769cc4409c29",
                "id": "UHJvamVjdDo1YjA1NDRjNTBlOGU3NjljYzQ0MDljMjk=",
                "name": "New-booking-Assistant",
                "desc": "demo purpose",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on May-23-2018 10:48:59."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2018-05-23T10:39:02.636Z"
            },
            {
                "_id": "5b4c6956c9a9b809e138e0b7",
                "id": "UHJvamVjdDo1YjRjNjk1NmM5YTliODA5ZTEzOGUwYjc=",
                "name": "demo-project",
                "desc": "demo purpose",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jul-18-2018 05:22:03."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2018-07-16T09:47:07.438Z"
            },
            {
                "_id": "5b92481f359c7f2417edd6c5",
                "id": "UHJvamVjdDo1YjkyNDgxZjM1OWM3ZjI0MTdlZGQ2YzU=",
                "name": "TestBot",
                "desc": "Matrimonial",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Sep-07-2018 10:49:29."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2018-09-07T09:43:14.346Z"
            },
            {
                "_id": "5b98b631ee011d7ae1aac820",
                "id": "UHJvamVjdDo1Yjk4YjYzMWVlMDExZDdhZTFhYWM4MjA=",
                "name": "Testbooking",
                "desc": "testing",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Sep-18-2018 11:04:34."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2018-09-12T06:46:24.636Z"
            },
            {
                "_id": "5badfd7cfc5bf109622d96ea",
                "id": "UHJvamVjdDo1YmFkZmQ3Y2ZjNWJmMTA5NjIyZDk2ZWE=",
                "name": "MasterDemo",
                "desc": "testing master greeting",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Sep-28-2018 10:14:21."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2018-09-28T10:08:06.288Z"
            },
            {
                "_id": "5b3f1163c34a360b9dab0541",
                "id": "UHJvamVjdDo1YjNmMTE2M2MzNGEzNjBiOWRhYjA1NDE=",
                "name": "testt-hello",
                "desc": "prod-test",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jul-09-2018 05:28:03."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2018-07-06T06:51:19.139Z"
            },
            {
                "_id": "5bf52edf35df3a6bd5e348d6",
                "id": "UHJvamVjdDo1YmY1MmVkZjM1ZGYzYTZiZDVlMzQ4ZDY=",
                "name": "TestAisleLocator",
                "desc": "This for Aisle locator",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2018-11-21T10:09:40.187Z"
            },
            {
                "_id": "5bf533d735df3a6bd5e3bfa2",
                "id": "UHJvamVjdDo1YmY1MzNkNzM1ZGYzYTZiZDVlM2JmYTI=",
                "name": "TestEntity",
                "desc": "TestEntity",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2018-11-21T10:30:47.883Z"
            },
            {
                "_id": "5bf5344835df3a6bd5e3c699",
                "id": "UHJvamVjdDo1YmY1MzQ0ODM1ZGYzYTZiZDVlM2M2OTk=",
                "name": "Intent-Issue-test",
                "desc": "test project",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2018-11-21T10:32:41.277Z"
            },
            {
                "_id": "5bf7a71935df3a6bd5ebdb54",
                "id": "UHJvamVjdDo1YmY3YTcxOTM1ZGYzYTZiZDVlYmRiNTQ=",
                "name": "MedicalAssistant-NovTest",
                "desc": "testing",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2018-11-23T07:07:06.482Z"
            },
            {
                "_id": "5bfbc0c435df3a6bd5f39852",
                "id": "UHJvamVjdDo1YmZiYzBjNDM1ZGYzYTZiZDVmMzk4NTI=",
                "name": "MedicalAssistant-Demo",
                "desc": "Demo project",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2018-11-26T09:45:40.674Z"
            },
            {
                "_id": "5bfcd03535df3a6bd5f8559b",
                "id": "UHJvamVjdDo1YmZjZDAzNTM1ZGYzYTZiZDVmODU1OWI=",
                "name": "hgjhghj",
                "desc": "wqweqwe",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2018-11-27T05:03:50.150Z"
            },
            {
                "_id": "5bfe5b0135df3a6bd5fd2777",
                "id": "UHJvamVjdDo1YmZlNWIwMTM1ZGYzYTZiZDVmZDI3Nzc=",
                "name": "MedicalAssistant-Test",
                "desc": "Demo project",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2018-11-28T09:08:50.190Z"
            },
            {
                "_id": "5c0e0ef735df3a6bd52cda95",
                "id": "UHJvamVjdDo1YzBlMGVmNzM1ZGYzYTZiZDUyY2RhOTU=",
                "name": "test-ascii",
                "desc": "testtt",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "training_failed",
                    "status_message": "expected string or buffer"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2018-12-10T07:00:09.558Z"
            },
            {
                "_id": "5c11dc5535df3a6bd53c387b",
                "id": "UHJvamVjdDo1YzExZGM1NTM1ZGYzYTZiZDUzYzM4N2I=",
                "name": "word2num",
                "desc": "word2num",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2018-12-13T04:13:09.873Z"
            },
            {
                "_id": "5afaa28a0e8e769cc429817e",
                "id": "UHJvamVjdDo1YWZhYTI4YTBlOGU3NjljYzQyOTgxN2U=",
                "name": "MedicalAssistant",
                "desc": "Medical Assistant bot for testing purpose",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2018-12-05T12:23:06.790Z"
            },
            {
                "_id": "5c2c687a6594a8026ca6affb",
                "id": "UHJvamVjdDo1YzJjNjg3YTY1OTRhODAyNmNhNmFmZmI=",
                "name": "xzxcsdv",
                "desc": "fdgvdfv",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-01-02T07:30:03.081Z"
            },
            {
                "_id": "5c08beb635df3a6bd5264e12",
                "id": "UHJvamVjdDo1YzA4YmViNjM1ZGYzYTZiZDUyNjRlMTI=",
                "name": "regex-adding",
                "desc": "sdvsdv",
                "ner": {
                    "status": "training_failed",
                    "status_message": "Not enough utterances for training"
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2018-12-06T06:16:23.003Z"
            },
            {
                "_id": "5c4014646594a8026cd15941",
                "id": "UHJvamVjdDo1YzQwMTQ2NDY1OTRhODAyNmNkMTU5NDE=",
                "name": "VAPT-Test",
                "desc": "jbdshbbhfsdhbjfsd",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-01-17T05:36:36.991Z"
            },
            {
                "_id": "5c501122d93bb76649cca4df",
                "id": "UHJvamVjdDo1YzUwMTEyMmQ5M2JiNzY2NDljY2E0ZGY=",
                "name": "bugFix",
                "desc": "longest match",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-01-29T08:39:00.326Z"
            },
            {
                "_id": "5c57c5846e08183753f8c311",
                "id": "UHJvamVjdDo1YzU3YzU4NDZlMDgxODM3NTNmOGMzMTE=",
                "name": "intenttest",
                "desc": "afasg",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-03-18T09:17:45.941Z"
            },
            {
                "_id": "5c01016535df3a6bd50e61aa",
                "id": "UHJvamVjdDo1YzAxMDE2NTM1ZGYzYTZiZDUwZTYxYWE=",
                "name": "ssssssssssssss",
                "desc": "eval(abcd)",
                "ner": {
                    "status": "training_failed",
                    "status_message": "Token mapping missing from training data"
                },
                "ir": {
                    "status": "training_failed",
                    "status_message": "expected string or buffer"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-01-15T05:45:44.121Z"
            },
            {
                "_id": "5cb5bb566e08183753f72c58",
                "id": "UHJvamVjdDo1Y2I1YmI1NjZlMDgxODM3NTNmNzJjNTg=",
                "name": "PasswordResetProject",
                "desc": "PasswordReset",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-04-16T11:24:07.563Z"
            },
            {
                "_id": "5cbd87f26e08183753ffdecc",
                "id": "UHJvamVjdDo1Y2JkODdmMjZlMDgxODM3NTNmZmRlY2M=",
                "name": "testprod4",
                "desc": "testprod4",
                "ner": {
                    "status": "training_failed",
                    "status_message": "Not enough utterances for training"
                },
                "ir": {
                    "status": "training_failed",
                    "status_message": "Add more intents for intent training"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-04-22T09:25:50.597Z"
            },
            {
                "_id": "5cbff5946e0818375302b7df",
                "id": "UHJvamVjdDo1Y2JmZjU5NDZlMDgxODM3NTMwMmI3ZGY=",
                "name": "testissue",
                "desc": "testissue",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-04-24T10:24:08.256Z"
            },
            {
                "_id": "5cc2c56a6e081837530c87c7",
                "id": "UHJvamVjdDo1Y2MyYzU2YTZlMDgxODM3NTMwYzg3Yzc=",
                "name": "masterr",
                "desc": "wedede",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-04-26T08:46:34.862Z"
            },
            {
                "_id": "5cd14c5f6e081837536ae2a2",
                "id": "UHJvamVjdDo1Y2QxNGM1ZjZlMDgxODM3NTM2YWUyYTI=",
                "name": "test-ss",
                "desc": "To test",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-05-07T09:14:08.898Z"
            },
            {
                "_id": "5cd2b5576e08183753782936",
                "id": "UHJvamVjdDo1Y2QyYjU1NzZlMDgxODM3NTM3ODI5MzY=",
                "name": "bug-fix-testing",
                "desc": "testing for patch",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-05-08T10:54:15.024Z"
            },
            {
                "_id": "5bd19ab4a973d070442356e2",
                "id": "UHJvamVjdDo1YmQxOWFiNGE5NzNkMDcwNDQyMzU2ZTI=",
                "name": "UITest",
                "desc": "ui testing",
                "ner": {
                    "status": "training_failed",
                    "status_message": "Unable to do entity training as no custom entities are mapped. Please map atleast 2 custom entities to proceed."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2018-10-25T10:28:04.852Z"
            },
            {
                "_id": "5cd2d5b36e08183753795e67",
                "id": "UHJvamVjdDo1Y2QyZDViMzZlMDgxODM3NTM3OTVlNjc=",
                "name": "demo-ss",
                "desc": "for demotest",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-05-08T13:12:20.352Z"
            },
            {
                "_id": "5cd926056e081837539cae26",
                "id": "UHJvamVjdDo1Y2Q5MjYwNTZlMDgxODM3NTM5Y2FlMjY=",
                "name": "testmasterbot",
                "desc": "testmasterbot",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-05-13T08:08:38.082Z"
            },
            {
                "_id": "5ce522646e08183753dc4349",
                "id": "UHJvamVjdDo1Y2U1MjI2NDZlMDgxODM3NTNkYzQzNDk=",
                "name": "testttttsynonym",
                "desc": "testtttttt",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-05-22T10:20:21.376Z"
            },
            {
                "_id": "5ce68cfccc2de34bff30d37d",
                "id": "UHJvamVjdDo1Y2U2OGNmY2NjMmRlMzRiZmYzMGQzN2Q=",
                "name": "testsynonymmay23",
                "desc": "testsynonymmay23",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-05-23T12:07:25.399Z"
            },
            {
                "_id": "5ce7c12747cf4e7274613839",
                "id": "UHJvamVjdDo1Y2U3YzEyNzQ3Y2Y0ZTcyNzQ2MTM4Mzk=",
                "name": "testspanish",
                "desc": "testspanish",
                "ner": {
                    "status": "training_failed",
                    "status_message": "Unable to do entity training as no custom entities are mapped. Please map atleast 2 custom entities to proceed."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-05-24T10:05:55.078Z"
            },
            {
                "_id": "5ce7dd2b47cf4e727461649d",
                "id": "UHJvamVjdDo1Y2U3ZGQyYjQ3Y2Y0ZTcyNzQ2MTY0OWQ=",
                "name": "FoodProcessingSystem",
                "desc": "FoodProcessingSystem",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-05-24T12:01:48.592Z"
            },
            {
                "_id": "5ceb8deb47cf4e727461fc1d",
                "id": "UHJvamVjdDo1Y2ViOGRlYjQ3Y2Y0ZTcyNzQ2MWZjMWQ=",
                "name": "test-clones-demo",
                "desc": "testing new ",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-05-27T07:12:46.894Z"
            },
            {
                "_id": "5b98dec8ee011d7ae1abd144",
                "id": "UHJvamVjdDo1Yjk4ZGVjOGVlMDExZDdhZTFhYmQxNDQ=",
                "name": "testimport2",
                "desc": "testimport2",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2018-10-25T14:19:55.828Z"
            },
            {
                "_id": "5bd2ebbfa973d070442acc77",
                "id": "UHJvamVjdDo1YmQyZWJiZmE5NzNkMDcwNDQyYWNjNzc=",
                "name": "MedicalAssistant-Spanish",
                "desc": "Spanish dataset for Medical Assistant",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2018-10-26T10:26:08.991Z"
            },
            {
                "_id": "5ce6401dcc2de34bff2cd14f",
                "id": "UHJvamVjdDo1Y2U2NDAxZGNjMmRlMzRiZmYyY2QxNGY=",
                "name": "test011",
                "desc": "testingg",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-05-23T06:39:29.114Z"
            },
            {
                "_id": "5cf0c8c2308aae6a1174c4e1",
                "id": "UHJvamVjdDo1Y2YwYzhjMjMwOGFhZTZhMTE3NGM0ZTE=",
                "name": "testbot",
                "desc": "testbot demo",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-05-31T06:25:07.808Z"
            },
            {
                "_id": "5cf649ce308aae6a11809e31",
                "id": "UHJvamVjdDo1Y2Y2NDljZTMwOGFhZTZhMTE4MDllMzE=",
                "name": "testchildbot",
                "desc": "testchildbot",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-06-04T10:37:03.472Z"
            },
            {
                "_id": "5cf8b0f6308aae6a11816bf0",
                "id": "UHJvamVjdDo1Y2Y4YjBmNjMwOGFhZTZhMTE4MTZiZjA=",
                "name": "BOT-DesignerTest",
                "desc": "BOT-DesignerTest",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-06-26T04:12:25.862Z"
            },
            {
                "_id": "5cfa4d15308aae6a118818b4",
                "id": "UHJvamVjdDo1Y2ZhNGQxNTMwOGFhZTZhMTE4ODE4YjQ=",
                "name": "DemoE2E-Resetpassword",
                "desc": "DemoE2E-Reset password",
                "ner": {
                    "status": "validated",
                    "status_message": "Validation completed successfully."
                },
                "ir": {
                    "status": "validated",
                    "status_message": "Validation completed successfully."
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-06-07T11:40:06.205Z"
            },
            {
                "_id": "5cfe40a4308aae6a118c0ffd",
                "id": "UHJvamVjdDo1Y2ZlNDBhNDMwOGFhZTZhMTE4YzBmZmQ=",
                "name": "bookingticket",
                "desc": "testing",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-06-10T11:36:05.868Z"
            },
            {
                "_id": "5d071cd4308aae6a119a0126",
                "id": "UHJvamVjdDo1ZDA3MWNkNDMwOGFhZTZhMTE5YTAxMjY=",
                "name": "devtesting",
                "desc": "dev testing 2",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-06-17T07:19:00.037Z"
            },
            {
                "_id": "5d072719308aae6a119a27b4",
                "id": "UHJvamVjdDo1ZDA3MjcxOTMwOGFhZTZhMTE5YTI3YjQ=",
                "name": "TestUtterance",
                "desc": "TestUtterance",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-06-17T05:37:30.888Z"
            },
            {
                "_id": "5d0752ee308aae6a119ae425",
                "id": "UHJvamVjdDo1ZDA3NTJlZTMwOGFhZTZhMTE5YWU0MjU=",
                "name": "devtesting1",
                "desc": "dev testing1",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-06-17T08:44:31.780Z"
            },
            {
                "_id": "5d136ce6144b3514032c94c2",
                "id": "UHJvamVjdDo1ZDEzNmNlNjE0NGIzNTE0MDMyYzk0YzI=",
                "name": "55454",
                "desc": "545454",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-06-26T13:02:31.091Z"
            },
            {
                "_id": "5d14645f144b3514032de994",
                "id": "UHJvamVjdDo1ZDE0NjQ1ZjE0NGIzNTE0MDMyZGU5OTQ=",
                "name": "srrt",
                "desc": "wehryrsjn ewh",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-06-27T06:38:24.496Z"
            },
            {
                "_id": "5d146560144b3514032e118c",
                "id": "UHJvamVjdDo1ZDE0NjU2MDE0NGIzNTE0MDMyZTExOGM=",
                "name": "qqqqdw",
                "desc": "wedfd",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "private",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-06-27T06:42:42.217Z"
            }
        ],
        "PublicProjects": [
            {
                "_id": "5952a1a1c9c57fd148d088eb",
                "id": "UHJvamVjdDo1OTUyYTFhMWM5YzU3ZmQxNDhkMDg4ZWI=",
                "name": "ATM-PIN-Reset",
                "desc": "Test - ATM PIN Reset",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Mar-27-2018 13:56:00."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-06-27T18:24:16.155Z"
            },
            {
                "_id": "59631e51c9c57fd148d089f0",
                "id": "UHJvamVjdDo1OTYzMWU1MWM5YzU3ZmQxNDhkMDg5ZjA=",
                "name": "satsuma",
                "desc": "Satsuma loans ",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Dec-19-2017 07:03:57."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-07-10T06:58:12.408Z"
            },
            {
                "_id": "5965a976c9c57fd148d08b8f",
                "id": "UHJvamVjdDo1OTY1YTk3NmM5YzU3ZmQxNDhkMDhiOGY=",
                "name": "example1",
                "desc": "example project",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Aug-08-2018 12:12:38."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "Intent recognition model published successfully on Aug-08-2018 12:12:35."
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-07-12T04:46:33.285Z"
            },
            {
                "_id": "5965bcb2c9c57fd148d08c4a",
                "id": "UHJvamVjdDo1OTY1YmNiMmM5YzU3ZmQxNDhkMDhjNGE=",
                "name": "intent-test",
                "desc": "intent-test",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-07-12T06:11:27.441Z"
            },
            {
                "_id": "59783cc2fc97be6468dbf981",
                "id": "UHJvamVjdDo1OTc4M2NjMmZjOTdiZTY0NjhkYmY5ODE=",
                "name": "resetpassword",
                "desc": "resetpassword",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jan-09-2018 08:13:21."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-07-26T06:56:07.342Z"
            },
            {
                "_id": "597853bbfc97be6468dbfad1",
                "id": "UHJvamVjdDo1OTc4NTNiYmZjOTdiZTY0NjhkYmZhZDE=",
                "name": "clonesResetpassword",
                "desc": "For clones testing - resetpassword flow - by Sarfaras",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Sep-13-2017 11:55:56."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-07-27T11:49:14.945Z"
            },
            {
                "_id": "5979a4d7fc97be6468dbfd1c",
                "id": "UHJvamVjdDo1OTc5YTRkN2ZjOTdiZTY0NjhkYmZkMWM=",
                "name": "Email",
                "desc": "To find the job error emails.",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Sep-13-2017 11:51:41."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-07-28T08:00:35.447Z"
            },
            {
                "_id": "5979c24efc97be6468dbfdf8",
                "id": "UHJvamVjdDo1OTc5YzI0ZWZjOTdiZTY0NjhkYmZkZjg=",
                "name": "PASSWORD",
                "desc": "RESET",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Sep-13-2017 11:16:10."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-07-27T10:42:18.087Z"
            },
            {
                "_id": "59899c752dddf78c7352e99e",
                "id": "UHJvamVjdDo1OTg5OWM3NTJkZGRmNzhjNzM1MmU5OWU=",
                "name": "WoltersKluwerService",
                "desc": "Wolters Kluwer Service Desk",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on May-29-2018 08:12:07."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-08-08T11:17:44.327Z"
            },
            {
                "_id": "598af8c92dddf78c7352edbe",
                "id": "UHJvamVjdDo1OThhZjhjOTJkZGRmNzhjNzM1MmVkYmU=",
                "name": "UMA",
                "desc": "NER to power UMA",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Oct-04-2017 08:34:18."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-08-09T13:05:14.563Z"
            },
            {
                "_id": "5993ed762dddf78c7352ef20",
                "id": "UHJvamVjdDo1OTkzZWQ3NjJkZGRmNzhjNzM1MmVmMjA=",
                "name": "WolterKluwerPOC",
                "desc": "WolterKluwerPOC",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Sep-25-2017 08:11:13."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-08-16T07:01:29.091Z"
            },
            {
                "_id": "59a7e8de4336f9ff03d22100",
                "id": "UHJvamVjdDo1OWE3ZThkZTQzMzZmOWZmMDNkMjIxMDA=",
                "name": "TravelRequest",
                "desc": "Travel Request",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-08-31T10:51:23.136Z"
            },
            {
                "_id": "59bb6420bf2a64c5c0bb3a9e",
                "id": "UHJvamVjdDo1OWJiNjQyMGJmMmE2NGM1YzBiYjNhOWU=",
                "name": "HealthCare",
                "desc": "HealthCare NER for finding nearest provider",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Sep-15-2017 05:46:49."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-09-15T05:27:14.723Z"
            },
            {
                "_id": "59ca0a3fbf2a64c5c0be1c98",
                "id": "UHJvamVjdDo1OWNhMGEzZmJmMmE2NGM1YzBiZTFjOTg=",
                "name": "JaideepTest",
                "desc": "Test Project",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Sep-27-2017 12:14:39."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "U33298"
                },
                "updatedAt": "2017-09-26T08:05:44.144Z"
            },
            {
                "_id": "59cddbd46c75b1e7dec8f014",
                "id": "UHJvamVjdDo1OWNkZGJkNDZjNzViMWU3ZGVjOGYwMTQ=",
                "name": "JAYANTEST",
                "desc": "Just for testing",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jan-04-2018 07:22:03."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-09-29T05:36:38.317Z"
            },
            {
                "_id": "59d467c56c75b1e7dec94789",
                "id": "UHJvamVjdDo1OWQ0NjdjNTZjNzViMWU3ZGVjOTQ3ODk=",
                "name": "DEMO",
                "desc": "Testing",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Oct-04-2017 08:44:05."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-10-04T04:47:13.313Z"
            },
            {
                "_id": "59df0d47df0d8943fc68f08f",
                "id": "UHJvamVjdDo1OWRmMGQ0N2RmMGQ4OTQzZmM2OGYwOGY=",
                "name": "deepthi",
                "desc": "Project created by Deepthi chandran for testing clones v3.2",
                "ner": {
                    "status": "trained",
                    "status_message": "Atleast 2 custom entities are mandatory to perform entity training. Please add one more custom entity to proceed."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-10-12T06:36:10.504Z"
            },
            {
                "_id": "59e05e64df0d8943fc68fbc6",
                "id": "UHJvamVjdDo1OWUwNWU2NGRmMGQ4OTQzZmM2OGZiYzY=",
                "name": "conversation-engine",
                "desc": "Conversation Engine",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Mar-22-2018 09:16:29."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": null,
                "updatedAt": "2017-10-13T06:34:55.929Z"
            },
            {
                "_id": "59e5d8a7df0d8943fc694856",
                "id": "UHJvamVjdDo1OWU1ZDhhN2RmMGQ4OTQzZmM2OTQ4NTY=",
                "name": "ramtest",
                "desc": "ramtesting with anthem app",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on May-11-2018 03:12:29."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-12-21T16:25:47.892Z"
            },
            {
                "_id": "5ab61411c9b8e8bacbcee0d7",
                "id": "UHJvamVjdDo1YWI2MTQxMWM5YjhlOGJhY2JjZWUwZDc=",
                "name": "ChatBotDemo",
                "desc": "ChatBot Demo Client",
                "ner": {
                    "status": "trained",
                    "status_message": "Atleast 2 custom entities are mandatory to perform entity training. Please add one more custom entity to proceed."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "innovationservices"
                },
                "updatedAt": "2018-03-24T09:03:08.498Z"
            },
            {
                "_id": "5ab8d964c9b8e8bacbd2bc7d",
                "id": "UHJvamVjdDo1YWI4ZDk2NGM5YjhlOGJhY2JkMmJjN2Q=",
                "name": "InnovationLabTestProject",
                "desc": "Test project for Innovation demo",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on May-11-2018 06:21:56."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "innovationservices"
                },
                "updatedAt": "2018-03-26T11:28:56.528Z"
            },
            {
                "_id": "5bcf0faae366630b19bdb8c0",
                "id": "UHJvamVjdDo1YmNmMGZhYWUzNjY2MzBiMTliZGI4YzA=",
                "name": "MipaNLP",
                "desc": "This is an NLP to identify and understand keywords",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Oct-24-2018 11:59:27."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "mipa"
                },
                "updatedAt": "2018-10-23T12:10:58.991Z"
            },
            {
                "_id": "5a01c5bdc8435ee1bc98bce2",
                "id": "UHJvamVjdDo1YTAxYzViZGM4NDM1ZWUxYmM5OGJjZTI=",
                "name": "BootsPOC",
                "desc": "Boots POC",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Nov-13-2017 15:47:59."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-11-13T09:23:25.413Z"
            },
            {
                "_id": "5a052feec8435ee1bc9bfd5f",
                "id": "UHJvamVjdDo1YTA1MmZlZWM4NDM1ZWUxYmM5YmZkNWY=",
                "name": "wish",
                "desc": "wish to someone",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Nov-10-2017 05:03:40."
                },
                "ir": {
                    "status": "training_failed",
                    "status_message": "argument 2 to map() must support iteration"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-11-10T04:50:27.407Z"
            },
            {
                "_id": "5a096c5c8063312a5c66b7d5",
                "id": "UHJvamVjdDo1YTA5NmM1YzgwNjMzMTJhNWM2NmI3ZDU=",
                "name": "Travels",
                "desc": "Travels",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Nov-13-2017 10:05:40."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-11-13T09:57:33.893Z"
            },
            {
                "_id": "5a129e3131121f93b722d1d6",
                "id": "UHJvamVjdDo1YTEyOWUzMTMxMTIxZjkzYjcyMmQxZDY=",
                "name": "serveraccess",
                "desc": "need access for server",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Nov-20-2017 11:58:08."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-11-20T09:19:59.413Z"
            },
            {
                "_id": "5c6fb90f6e0818375380e0dc",
                "id": "UHJvamVjdDo1YzZmYjkwZjZlMDgxODM3NTM4MGUwZGM=",
                "name": "travelbotsample",
                "desc": "sample bot for AF testing",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "varun"
                },
                "updatedAt": "2019-05-24T06:04:01.111Z"
            },
            {
                "_id": "5d120af0308aae6a11b9126f",
                "id": "UHJvamVjdDo1ZDEyMGFmMDMwOGFhZTZhMTFiOTEyNmY=",
                "name": "TestDelete",
                "desc": "Delete test ",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-06-25T11:52:17.409Z"
            },
            {
                "_id": "59e5822adf0d8943fc692bd4",
                "id": "UHJvamVjdDo1OWU1ODIyYWRmMGQ4OTQzZmM2OTJiZDQ=",
                "name": "Test123",
                "desc": "Test123",
                "ner": {
                    "status": "trained",
                    "status_message": "Atleast 2 custom entities are mandatory to perform entity training. Please add one more custom entity to proceed."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-10-17T04:09:23.390Z"
            },
            {
                "_id": "59e85bb5df0d8943fc69b524",
                "id": "UHJvamVjdDo1OWU4NWJiNWRmMGQ4OTQzZmM2OWI1MjQ=",
                "name": "Boots",
                "desc": "Boots",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Oct-25-2017 06:55:51."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-10-19T08:04:31.890Z"
            },
            {
                "_id": "59e991e7df0d8943fc6a1758",
                "id": "UHJvamVjdDo1OWU5OTFlN2RmMGQ4OTQzZmM2YTE3NTg=",
                "name": "Test-SreekanthC",
                "desc": "Project created for testing purpose",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Oct-20-2017 10:37:11."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-10-20T07:09:20.782Z"
            },
            {
                "_id": "59edd24fdf0d8943fc6ad613",
                "id": "UHJvamVjdDo1OWVkZDI0ZmRmMGQ4OTQzZmM2YWQ2MTM=",
                "name": "chatbot",
                "desc": "Create utterances for chat bot ",
                "ner": {
                    "status": "trained",
                    "status_message": "Atleast 2 custom entities are mandatory to perform entity training. Please add one more custom entity to proceed."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "anishmelbin"
                },
                "updatedAt": "2017-10-23T11:31:25.557Z"
            },
            {
                "_id": "59f0789ddf0d8943fc6b25f2",
                "id": "UHJvamVjdDo1OWYwNzg5ZGRmMGQ4OTQzZmM2YjI1ZjI=",
                "name": "helloworld",
                "desc": "a hello world application for the beginners",
                "ner": {
                    "status": "training_failed",
                    "status_message": "Unable to do entity training as no custom entities are mapped. Please map atleast 2 custom entities to proceed."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "clones"
                },
                "updatedAt": "2017-10-25T11:42:29.751Z"
            },
            {
                "_id": "59f2bae4df0d8943fc6b7a8f",
                "id": "UHJvamVjdDo1OWYyYmFlNGRmMGQ4OTQzZmM2YjdhOGY=",
                "name": "MyDoc",
                "desc": "MyDoc Chatbot",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "Prabitha"
                },
                "updatedAt": "2017-10-27T04:50:16.423Z"
            },
            {
                "_id": "59f30567df0d8943fc6b9ca9",
                "id": "UHJvamVjdDo1OWYzMDU2N2RmMGQ4OTQzZmM2YjljYTk=",
                "name": "SAMPLETEST",
                "desc": "sample app",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Dec-19-2017 07:03:46."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-10-27T10:08:08.123Z"
            },
            {
                "_id": "59f6ec28df0d8943fc6c1785",
                "id": "UHJvamVjdDo1OWY2ZWMyOGRmMGQ4OTQzZmM2YzE3ODU=",
                "name": "cloneshelloworld",
                "desc": "helloworld for clones - sarf",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Dec-01-2017 06:47:42."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-10-30T09:09:24.431Z"
            },
            {
                "_id": "59f8622edf0d8943fc6ca485",
                "id": "UHJvamVjdDo1OWY4NjIyZWRmMGQ4OTQzZmM2Y2E0ODU=",
                "name": "Mydeen123",
                "desc": "creating project for training purpose",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Nov-13-2017 06:44:37."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-10-31T11:45:21.747Z"
            },
            {
                "_id": "59f99ff5df0d8943fc6d1ff7",
                "id": "UHJvamVjdDo1OWY5OWZmNWRmMGQ4OTQzZmM2ZDFmZjc=",
                "name": "DemoTraining",
                "desc": "demo training",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jun-05-2018 07:24:02."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-11-01T10:20:57.009Z"
            },
            {
                "_id": "59fd604b3bbf886d100ef485",
                "id": "UHJvamVjdDo1OWZkNjA0YjNiYmY4ODZkMTAwZWY0ODU=",
                "name": "bootsResetPassword",
                "desc": "This is for Boots Password.",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Nov-07-2017 14:19:14."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-11-04T06:38:58.277Z"
            },
            {
                "_id": "59fe1c673bbf886d101017ae",
                "id": "UHJvamVjdDo1OWZlMWM2NzNiYmY4ODZkMTAxMDE3YWU=",
                "name": "sapsrmbootspasswordreset",
                "desc": "SAP SRM Password Reset",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Nov-05-2017 10:08:13."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-11-04T21:33:06.667Z"
            },
            {
                "_id": "5a00061a745faecb410f39c2",
                "id": "UHJvamVjdDo1YTAwMDYxYTc0NWZhZWNiNDEwZjM5YzI=",
                "name": "demo2",
                "desc": "this is for training",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Nov-21-2017 07:01:17."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-11-06T06:50:21.679Z"
            },
            {
                "_id": "5a053e76c8435ee1bc9d12a9",
                "id": "UHJvamVjdDo1YTA1M2U3NmM4NDM1ZWUxYmM5ZDEyYTk=",
                "name": "QAAdvisor",
                "desc": "QAAdvisor",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Nov-15-2017 09:44:10."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-11-15T05:57:46.812Z"
            },
            {
                "_id": "5a057027c8435ee1bc9e8f86",
                "id": "UHJvamVjdDo1YTA1NzAyN2M4NDM1ZWUxYmM5ZThmODY=",
                "name": "College",
                "desc": "College",
                "ner": {
                    "status": "trained",
                    "status_message": "Unable to do entity training as no custom entities are mapped. Please map atleast 2 custom entities to proceed."
                },
                "ir": {
                    "status": "training_failed",
                    "status_message": "argument 2 to map() must support iteration"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-11-10T09:24:37.050Z"
            },
            {
                "_id": "5a057241c8435ee1bc9ecaa8",
                "id": "UHJvamVjdDo1YTA1NzI0MWM4NDM1ZWUxYmM5ZWNhYTg=",
                "name": "test-nicy",
                "desc": "testing",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "training_failed",
                    "status_message": "argument 2 to map() must support iteration"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-11-10T09:33:18.791Z"
            },
            {
                "_id": "5a05767ac8435ee1bc9f4e1c",
                "id": "UHJvamVjdDo1YTA1NzY3YWM4NDM1ZWUxYmM5ZjRlMWM=",
                "name": "BootsChat",
                "desc": "chat for boots password reset",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Nov-27-2017 05:33:39."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-11-13T06:46:02.497Z"
            },
            {
                "_id": "5a058cd2c8435ee1bc9fbe7f",
                "id": "UHJvamVjdDo1YTA1OGNkMmM4NDM1ZWUxYmM5ZmJlN2Y=",
                "name": "test-nc",
                "desc": "testing",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Nov-10-2017 11:48:14."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-11-27T10:47:56.392Z"
            },
            {
                "_id": "5a0947208063312a5c637a7b",
                "id": "UHJvamVjdDo1YTA5NDcyMDgwNjMzMTJhNWM2MzdhN2I=",
                "name": "AutOpsLearning",
                "desc": "Learning",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Nov-13-2017 13:41:17."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-11-13T07:18:04.698Z"
            },
            {
                "_id": "5a0954cf8063312a5c65cd10",
                "id": "UHJvamVjdDo1YTA5NTRjZjgwNjMzMTJhNWM2NWNkMTA=",
                "name": "testTraining",
                "desc": "This is a test project for training purpose.",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-11-13T08:17:11.506Z"
            },
            {
                "_id": "5a095f588063312a5c66947c",
                "id": "UHJvamVjdDo1YTA5NWY1ODgwNjMzMTJhNWM2Njk0N2M=",
                "name": "appledemo",
                "desc": "appledemo",
                "ner": {
                    "status": "trained",
                    "status_message": "Unable to do entity training as no custom entities are mapped. Please map atleast 2 custom entities to proceed."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": null,
                "updatedAt": "2017-11-13T09:01:24.473Z"
            },
            {
                "_id": "5a0ea363637019237e71e7ee",
                "id": "UHJvamVjdDo1YTBlYTM2MzYzNzAxOTIzN2U3MWU3ZWU=",
                "name": "PacificDental-Learning",
                "desc": "PacificDental-Learning",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Nov-21-2017 04:34:19."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-11-17T09:06:27.101Z"
            },
            {
                "_id": "5a13c85531121f93b723c865",
                "id": "UHJvamVjdDo1YTEzYzg1NTMxMTIxZjkzYjcyM2M4NjU=",
                "name": "Anthem-BPO-RFC",
                "desc": "Anthem BPO RFC",
                "ner": {
                    "status": "trained",
                    "status_message": "Unable to do entity training as no custom entities are mapped. Please map atleast 2 custom entities to proceed."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-11-21T06:42:36.182Z"
            },
            {
                "_id": "5a15471631121f93b726809a",
                "id": "UHJvamVjdDo1YTE1NDcxNjMxMTIxZjkzYjcyNjgwOWE=",
                "name": "AnthemBPO-PasswordReset",
                "desc": "AnthemBPO-PasswordReset",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Mar-27-2018 06:55:22."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-11-22T09:45:14.561Z"
            },
            {
                "_id": "5a278a86fba8195fe9580d29",
                "id": "UHJvamVjdDo1YTI3OGE4NmZiYTgxOTVmZTk1ODBkMjk=",
                "name": "woltersk",
                "desc": "for wolters kluwer - Sarfaras",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Feb-05-2018 11:57:39."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-12-06T06:14:18.805Z"
            },
            {
                "_id": "5a27b77ffba8195fe958315e",
                "id": "UHJvamVjdDo1YTI3Yjc3ZmZiYTgxOTVmZTk1ODMxNWU=",
                "name": "Example",
                "desc": "products",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-12-06T09:25:42.670Z"
            },
            {
                "_id": "5a311485fba8195fe9600187",
                "id": "UHJvamVjdDo1YTMxMTQ4NWZiYTgxOTVmZTk2MDAxODc=",
                "name": "state-street-test",
                "desc": "created for state street test ",
                "ner": {
                    "status": "trained",
                    "status_message": "Atleast 2 custom entities are mandatory to perform entity training. Please add one more custom entity to proceed."
                },
                "ir": {
                    "status": "training_failed",
                    "status_message": "Add more intents for intent training"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-12-13T11:53:04.762Z"
            },
            {
                "_id": "5a3b40b54e0d078010489222",
                "id": "UHJvamVjdDo1YTNiNDBiNTRlMGQwNzgwMTA0ODkyMjI=",
                "name": "Testing-Sreejesh",
                "desc": "Testing-Sreejesh",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training is in progress."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-12-21T05:03:55.179Z"
            },
            {
                "_id": "5a3b410a4e0d078010489589",
                "id": "UHJvamVjdDo1YTNiNDEwYTRlMGQwNzgwMTA0ODk1ODk=",
                "name": "Greetings",
                "desc": "Greetings project for testing ICE",
                "ner": {
                    "status": "trained",
                    "status_message": "Atleast 2 custom entities are mandatory to perform entity training. Please add one more custom entity to proceed."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-12-21T05:11:20.534Z"
            },
            {
                "_id": "5a3b48e54e0d07801048b103",
                "id": "UHJvamVjdDo1YTNiNDhlNTRlMGQwNzgwMTA0OGIxMDM=",
                "name": "JiraTicketCreation",
                "desc": "This project is trained for new Jira ticket creation",
                "ner": {
                    "status": "trained",
                    "status_message": "Unable to do entity training as no custom entities are mapped. Please map atleast 2 custom entities to proceed."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-12-21T05:39:06.755Z"
            },
            {
                "_id": "5a3b50ad4e0d07801048b67e",
                "id": "UHJvamVjdDo1YTNiNTBhZDRlMGQwNzgwMTA0OGI2N2U=",
                "name": "Jiratest",
                "desc": "testing whether can able to generate the ticket or not ",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Dec-21-2017 06:15:39."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-12-21T06:12:09.754Z"
            },
            {
                "_id": "5a3be10a4e0d0780104bd7b9",
                "id": "UHJvamVjdDo1YTNiZTEwYTRlMGQwNzgwMTA0YmQ3Yjk=",
                "name": "WaltersKluwer-Corpus",
                "desc": "WaltersKluwer-Corpus Final",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Dec-22-2017 08:34:18."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-12-21T16:28:11.827Z"
            },
            {
                "_id": "5a3ccec44e0d07801051d5a7",
                "id": "UHJvamVjdDo1YTNjY2VjNDRlMGQwNzgwMTA1MWQ1YTc=",
                "name": "dummy",
                "desc": "dummy to test boots password reset for store domain",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jan-02-2018 04:01:48."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-12-22T09:22:30.079Z"
            },
            {
                "_id": "5a3e252c4e0d07801052d1a7",
                "id": "UHJvamVjdDo1YTNlMjUyYzRlMGQwNzgwMTA1MmQxYTc=",
                "name": "WK-EntityExtraction",
                "desc": "ENtity Extraction for WK",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-12-23T09:43:14.942Z"
            },
            {
                "_id": "5a44a9774e0d0780105b1214",
                "id": "UHJvamVjdDo1YTQ0YTk3NzRlMGQwNzgwMTA1YjEyMTQ=",
                "name": "ProductIdentification",
                "desc": "ProductIdentification",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jan-31-2018 07:28:45."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-12-28T08:21:36.857Z"
            },
            {
                "_id": "5a45d6c84e0d0780105d0d19",
                "id": "UHJvamVjdDo1YTQ1ZDZjODRlMGQwNzgwMTA1ZDBkMTk=",
                "name": "boots-skypechat",
                "desc": "this is sales and order related training process",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jan-08-2018 10:55:04."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": null,
                "updatedAt": "2017-12-29T05:47:34.632Z"
            },
            {
                "_id": "5a531e5a4e0d078010636ffb",
                "id": "UHJvamVjdDo1YTUzMWU1YTRlMGQwNzgwMTA2MzZmZmI=",
                "name": "bootssapbusinessobjs",
                "desc": "Boots SAP Business Objects",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jan-08-2018 10:37:42."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2018-01-08T07:31:49.411Z"
            },
            {
                "_id": "5a545e7d4e0d07801066a2b0",
                "id": "UHJvamVjdDo1YTU0NWU3ZDRlMGQwNzgwMTA2NmEyYjA=",
                "name": "bootscentredomain",
                "desc": "bootscentredomain",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jan-09-2018 06:42:37."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2018-01-09T06:17:41.334Z"
            },
            {
                "_id": "5a5595f04e0d078010693355",
                "id": "UHJvamVjdDo1YTU1OTVmMDRlMGQwNzgwMTA2OTMzNTU=",
                "name": "ICEXDTest",
                "desc": "Testing",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jan-11-2018 09:34:51."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2018-01-10T04:27:13.604Z"
            },
            {
                "_id": "5a55a24c4e0d0780106a0acf",
                "id": "UHJvamVjdDo1YTU1YTI0YzRlMGQwNzgwMTA2YTBhY2Y=",
                "name": "ICEXDTesting",
                "desc": "Testing ICE",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Mar-27-2018 06:33:41."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2018-01-10T05:19:19.367Z"
            },
            {
                "_id": "5a574a0c46b5b87be7ee8ea1",
                "id": "UHJvamVjdDo1YTU3NGEwYzQ2YjViODdiZTdlZThlYTE=",
                "name": "BootsSalesOrderChatbot",
                "desc": "Boots Sales Order Chatbot",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jan-22-2018 11:25:07."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "unni"
                },
                "updatedAt": "2018-01-11T11:27:59.297Z"
            },
            {
                "_id": "5a5e2b9b46b5b87be7f7d4fc",
                "id": "UHJvamVjdDo1YTVlMmI5YjQ2YjViODdiZTdmN2Q0ZmM=",
                "name": "Healthcare",
                "desc": "Demonstrate a simple usecase",
                "ner": {
                    "status": "trained",
                    "status_message": "Token mapping missing from training data"
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "deepa"
                },
                "updatedAt": "2018-01-16T17:06:17.627Z"
            },
            {
                "_id": "5a6079ec27aacd44abbabd31",
                "id": "UHJvamVjdDo1YTYwNzllYzI3YWFjZDQ0YWJiYWJkMzE=",
                "name": "Testissue",
                "desc": "Issue test",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jan-18-2018 10:56:55."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2018-01-18T10:42:00.676Z"
            },
            {
                "_id": "5a60a94527aacd44abbad0e2",
                "id": "UHJvamVjdDo1YTYwYTk0NTI3YWFjZDQ0YWJiYWQwZTI=",
                "name": "CMTest",
                "desc": "CMTest",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jan-19-2018 13:53:29."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2018-01-18T14:04:00.565Z"
            },
            {
                "_id": "5a633f5427aacd44abbbd9a0",
                "id": "UHJvamVjdDo1YTYzM2Y1NDI3YWFjZDQ0YWJiYmQ5YTA=",
                "name": "CMTrainTest",
                "desc": "CMTrainTest",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jan-20-2018 13:15:34."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2018-01-20T13:08:47.423Z"
            },
            {
                "_id": "5a65798d27aacd44abbd8de7",
                "id": "UHJvamVjdDo1YTY1Nzk4ZDI3YWFjZDQ0YWJiZDhkZTc=",
                "name": "CMDemotest",
                "desc": "CMDemotest",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jan-22-2018 07:56:57."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2018-01-22T05:41:36.783Z"
            },
            {
                "_id": "5a6604c727aacd44abc0b4e4",
                "id": "UHJvamVjdDo1YTY2MDRjNzI3YWFjZDQ0YWJjMGI0ZTQ=",
                "name": "CMWAImport",
                "desc": "CMWAImport",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jan-22-2018 15:37:02."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2018-01-22T15:35:38.444Z"
            },
            {
                "_id": "5a702b7f27aacd44abcea1ce",
                "id": "UHJvamVjdDo1YTcwMmI3ZjI3YWFjZDQ0YWJjZWExY2U=",
                "name": "UPSCompetitorAnalytics",
                "desc": "UPSCompetitorAnalytics",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jan-30-2018 10:24:38."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2018-01-30T08:23:39.994Z"
            },
            {
                "_id": "5a7150a927aacd44abd0727b",
                "id": "UHJvamVjdDo1YTcxNTBhOTI3YWFjZDQ0YWJkMDcyN2I=",
                "name": "Sample1",
                "desc": "test1",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-01-31T05:14:29.670Z"
            },
            {
                "_id": "5a740bad27aacd44abd8ecec",
                "id": "UHJvamVjdDo1YTc0MGJhZDI3YWFjZDQ0YWJkOGVjZWM=",
                "name": "Test1",
                "desc": "just testing",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Feb-07-2018 13:45:05."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-02-02T11:28:25.262Z"
            },
            {
                "_id": "5a781cd927aacd44abdb2a6a",
                "id": "UHJvamVjdDo1YTc4MWNkOTI3YWFjZDQ0YWJkYjJhNmE=",
                "name": "Trial1",
                "desc": "Trial 1 chatbot",
                "ner": {
                    "status": "trained",
                    "status_message": "Unable to do entity training as no custom entities are mapped. Please map atleast 2 custom entities to proceed."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-02-05T08:59:16.425Z"
            },
            {
                "_id": "5a79c90c27aacd44abe08fa9",
                "id": "UHJvamVjdDo1YTc5YzkwYzI3YWFjZDQ0YWJlMDhmYTk=",
                "name": "robertoTEST",
                "desc": "Roberto testing",
                "ner": {
                    "status": "trained",
                    "status_message": "Atleast 2 custom entities are mandatory to perform entity training. Please add one more custom entity to proceed."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "raceballos"
                },
                "updatedAt": "2018-02-06T15:34:48.543Z"
            },
            {
                "_id": "5a7c403927aacd44abe81a25",
                "id": "UHJvamVjdDo1YTdjNDAzOTI3YWFjZDQ0YWJlODFhMjU=",
                "name": "TestBOT",
                "desc": "check",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Feb-12-2018 04:47:10."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "u55616"
                },
                "updatedAt": "2018-02-09T10:14:47.511Z"
            },
            {
                "_id": "5a7d3d7a27aacd44abeb4da4",
                "id": "UHJvamVjdDo1YTdkM2Q3YTI3YWFjZDQ0YWJlYjRkYTQ=",
                "name": "DocChat",
                "desc": "testing",
                "ner": {
                    "status": "trained",
                    "status_message": "Token mapping missing from training data"
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-02-09T06:27:40.502Z"
            },
            {
                "_id": "5a7d476127aacd44abeb7bc0",
                "id": "UHJvamVjdDo1YTdkNDc2MTI3YWFjZDQ0YWJlYjdiYzA=",
                "name": "MedTest",
                "desc": "testing",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Feb-12-2018 14:26:48."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-02-09T07:01:58.873Z"
            },
            {
                "_id": "5a7d550627aacd44abeb82b0",
                "id": "UHJvamVjdDo1YTdkNTUwNjI3YWFjZDQ0YWJlYjgyYjA=",
                "name": "Costco-category-product",
                "desc": "Find category, brand and product",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Feb-12-2018 05:47:19."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "smitha"
                },
                "updatedAt": "2018-02-09T08:00:31.534Z"
            },
            {
                "_id": "5a817d8027aacd44abf449e0",
                "id": "UHJvamVjdDo1YTgxN2Q4MDI3YWFjZDQ0YWJmNDQ5ZTA=",
                "name": "chatshop",
                "desc": "chatting shop for any fields",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Feb-12-2018 12:01:02."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-02-12T11:42:24.634Z"
            },
            {
                "_id": "5a82783127aacd44abf66612",
                "id": "UHJvamVjdDo1YTgyNzgzMTI3YWFjZDQ0YWJmNjY2MTI=",
                "name": "phonedetails",
                "desc": "details about mobile phones",
                "ner": {
                    "status": "trained",
                    "status_message": "Atleast 2 custom entities are mandatory to perform entity training. Please add one more custom entity to proceed."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-02-13T05:32:34.165Z"
            },
            {
                "_id": "5a827fff27aacd44abf6eef7",
                "id": "UHJvamVjdDo1YTgyN2ZmZjI3YWFjZDQ0YWJmNmVlZjc=",
                "name": "Alexa-Demo1",
                "desc": "To develop skills for Alexa",
                "ner": {
                    "status": "trained",
                    "status_message": "Unable to do entity training as no custom entities are mapped. Please map atleast 2 custom entities to proceed."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "LizGeorge"
                },
                "updatedAt": "2018-02-13T06:06:55.728Z"
            },
            {
                "_id": "5a8334b427aacd44abfb5e10",
                "id": "UHJvamVjdDo1YTgzMzRiNDI3YWFjZDQ0YWJmYjVlMTA=",
                "name": "SSTest-AS",
                "desc": "Test for State Street and Weather for ICE Training - Aswath",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on May-07-2018 18:50:39."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2018-02-13T23:56:07.752Z"
            },
            {
                "_id": "5a83c15627aacd44abfc8c3d",
                "id": "UHJvamVjdDo1YTgzYzE1NjI3YWFjZDQ0YWJmYzhjM2Q=",
                "name": "MedDeliveryBot",
                "desc": "Medicinal delivery based on symptoms.",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Feb-15-2018 04:50:31."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "DIPIN"
                },
                "updatedAt": "2018-02-14T04:55:59.776Z"
            },
            {
                "_id": "5a85006a27aacd44ab002213",
                "id": "UHJvamVjdDo1YTg1MDA2YTI3YWFjZDQ0YWIwMDIyMTM=",
                "name": "DentalAssistant",
                "desc": "Dental Assistant",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jun-19-2018 20:03:42."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2018-02-15T03:37:23.175Z"
            },
            {
                "_id": "5a85025027aacd44ab003740",
                "id": "UHJvamVjdDo1YTg1MDI1MDI3YWFjZDQ0YWIwMDM3NDA=",
                "name": "PatientPortal",
                "desc": "Patient Portal",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jun-21-2018 20:43:58."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2018-02-15T03:58:28.370Z"
            },
            {
                "_id": "5a852d7627aacd44ab009f51",
                "id": "UHJvamVjdDo1YTg1MmQ3NjI3YWFjZDQ0YWIwMDlmNTE=",
                "name": "cab",
                "desc": "testing",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Feb-16-2018 10:06:43."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-02-15T06:49:58.257Z"
            },
            {
                "_id": "5a86b80e27aacd44ab06c2f9",
                "id": "UHJvamVjdDo1YTg2YjgwZTI3YWFjZDQ0YWIwNmMyZjk=",
                "name": "foodbevarages",
                "desc": "chatdemo",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Feb-16-2018 17:19:15."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-02-16T10:53:18.425Z"
            },
            {
                "_id": "5a86d04027aacd44ab07258c",
                "id": "UHJvamVjdDo1YTg2ZDA0MDI3YWFjZDQ0YWIwNzI1OGM=",
                "name": "Travel-planner",
                "desc": "Chat bot to plan my travel",
                "ner": {
                    "status": "trained",
                    "status_message": "Unable to do entity training as no custom entities are mapped. Please map atleast 2 custom entities to proceed."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2018-02-16T12:37:00.968Z"
            },
            {
                "_id": "5a892a9327aacd44ab07cf2d",
                "id": "UHJvamVjdDo1YTg5MmE5MzI3YWFjZDQ0YWIwN2NmMmQ=",
                "name": "PizzaBot",
                "desc": "Pizza delivery",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Feb-20-2018 16:08:28."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-02-18T07:29:19.430Z"
            },
            {
                "_id": "5a8a781a27aacd44ab094fd3",
                "id": "UHJvamVjdDo1YThhNzgxYTI3YWFjZDQ0YWIwOTRmZDM=",
                "name": "Aditi1",
                "desc": "aditi 1 is a conversational platform",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Feb-19-2018 07:31:39."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-02-19T07:09:22.188Z"
            },
            {
                "_id": "5a8a791627aacd44ab09a027",
                "id": "UHJvamVjdDo1YThhNzkxNjI3YWFjZDQ0YWIwOWEwMjc=",
                "name": "alexa",
                "desc": "integration",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Feb-21-2018 04:13:46."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "aswini"
                },
                "updatedAt": "2018-02-19T07:16:16.567Z"
            },
            {
                "_id": "5a8a79d727aacd44ab09be45",
                "id": "UHJvamVjdDo1YThhNzlkNzI3YWFjZDQ0YWIwOWJlNDU=",
                "name": "Ice-Integration-V1",
                "desc": "Demo for the Integration of Alexa with ICE.XD",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Feb-20-2018 09:53:32."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "LizGeorge"
                },
                "updatedAt": "2018-02-19T07:16:57.041Z"
            },
            {
                "_id": "5a8a99c827aacd44ab0a8860",
                "id": "UHJvamVjdDo1YThhOTljODI3YWFjZDQ0YWIwYTg4NjA=",
                "name": "Try001",
                "desc": "Building Chat bot for alexa skill",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Feb-20-2018 04:38:22."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "Anju"
                },
                "updatedAt": "2018-02-19T09:33:04.801Z"
            },
            {
                "_id": "5a8baed527aacd44ab1481bd",
                "id": "UHJvamVjdDo1YThiYWVkNTI3YWFjZDQ0YWIxNDgxYmQ=",
                "name": "Ice-Integration-V2",
                "desc": "ICE integration TRial 2",
                "ner": {
                    "status": "trained",
                    "status_message": "Unable to do entity training as no custom entities are mapped. Please map atleast 2 custom entities to proceed."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "LizGeorge"
                },
                "updatedAt": "2018-02-20T05:15:27.060Z"
            },
            {
                "_id": "5a8bb97b27aacd44ab15052f",
                "id": "UHJvamVjdDo1YThiYjk3YjI3YWFjZDQ0YWIxNTA1MmY=",
                "name": "sharedriveaccess",
                "desc": "testing to get access to shred drive",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Feb-20-2018 07:28:36."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-02-20T06:00:38.644Z"
            },
            {
                "_id": "5a8bcfa927aacd44ab1559ff",
                "id": "UHJvamVjdDo1YThiY2ZhOTI3YWFjZDQ0YWIxNTU5ZmY=",
                "name": "intakereq",
                "desc": "testreq",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Feb-20-2018 17:44:25."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-02-20T07:35:31.210Z"
            },
            {
                "_id": "5a8bf1ff27aacd44ab165ec6",
                "id": "UHJvamVjdDo1YThiZjFmZjI3YWFjZDQ0YWIxNjVlYzY=",
                "name": "StudentRegistration",
                "desc": "Registration Demo",
                "ner": {
                    "status": "trained",
                    "status_message": "Unable to do entity training as no custom entities are mapped. Please map atleast 2 custom entities to proceed."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "LizGeorge"
                },
                "updatedAt": "2018-02-20T10:01:46.891Z"
            },
            {
                "_id": "5a8cf83027aacd44ab17e385",
                "id": "UHJvamVjdDo1YThjZjgzMDI3YWFjZDQ0YWIxN2UzODU=",
                "name": "studious",
                "desc": "alexachatbot",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Feb-21-2018 05:00:07."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "aswini"
                },
                "updatedAt": "2018-02-21T04:40:28.020Z"
            },
            {
                "_id": "5a8d21ab27aacd44ab18f497",
                "id": "UHJvamVjdDo1YThkMjFhYjI3YWFjZDQ0YWIxOGY0OTc=",
                "name": "Alexaintegration-update",
                "desc": "Alexa Integrations",
                "ner": {
                    "status": "trained",
                    "status_message": "Unable to do entity training as no custom entities are mapped. Please map atleast 2 custom entities to proceed."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-02-21T07:37:25.523Z"
            },
            {
                "_id": "5a8d4b9327aacd44ab19471e",
                "id": "UHJvamVjdDo1YThkNGI5MzI3YWFjZDQ0YWIxOTQ3MWU=",
                "name": "uitra",
                "desc": "trying new ui ",
                "ner": {
                    "status": "trained",
                    "status_message": "Unable to do entity training as no custom entities are mapped. Please map atleast 2 custom entities to proceed."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-02-21T10:36:12.712Z"
            },
            {
                "_id": "5a8d882327aacd44ab1a1223",
                "id": "UHJvamVjdDo1YThkODgyMzI3YWFjZDQ0YWIxYTEyMjM=",
                "name": "time",
                "desc": "testing ui change",
                "ner": {
                    "status": "trained",
                    "status_message": "Unable to do entity training as no custom entities are mapped. Please map atleast 2 custom entities to proceed."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-02-21T14:54:37.734Z"
            },
            {
                "_id": "5a8e40bc27aacd44ab1a3627",
                "id": "UHJvamVjdDo1YThlNDBiYzI3YWFjZDQ0YWIxYTM2Mjc=",
                "name": "abcd",
                "desc": "fdsdffr",
                "ner": {
                    "status": "trained",
                    "status_message": "Unable to do entity training as no custom entities are mapped. Please map atleast 2 custom entities to proceed."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-02-22T04:02:09.729Z"
            },
            {
                "_id": "5a95035027aacd44ab29b377",
                "id": "UHJvamVjdDo1YTk1MDM1MDI3YWFjZDQ0YWIyOWIzNzc=",
                "name": "wallmart-train",
                "desc": "Training of NER in walmart dataset",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Mar-24-2018 05:41:47."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2018-02-27T07:08:15.795Z"
            },
            {
                "_id": "5a97a91e27aacd44ab32aeed",
                "id": "UHJvamVjdDo1YTk3YTkxZTI3YWFjZDQ0YWIzMmFlZWQ=",
                "name": "wallmart-train-1",
                "desc": "NER on small dataset",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Mar-01-2018 10:14:51."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2018-03-01T09:35:37.470Z"
            },
            {
                "_id": "5a9d67df27aacd44ab37054e",
                "id": "UHJvamVjdDo1YTlkNjdkZjI3YWFjZDQ0YWIzNzA1NGU=",
                "name": "UTC",
                "desc": "UTC Visit",
                "ner": {
                    "status": "trained",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-03-05T15:53:11.060Z"
            },
            {
                "_id": "5a9e53fb27aacd44ab3c7c3b",
                "id": "UHJvamVjdDo1YTllNTNmYjI3YWFjZDQ0YWIzYzdjM2I=",
                "name": "KochiInfinity",
                "desc": "alexa icexd use case",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jun-05-2018 12:29:55."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-03-06T08:40:52.629Z"
            },
            {
                "_id": "5a3b3c3a4e0d078010485109",
                "id": "UHJvamVjdDo1YTNiM2MzYTRlMGQwNzgwMTA0ODUxMDk=",
                "name": "SampleDemo",
                "desc": "This is demo project",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "anuazeez"
                },
                "updatedAt": "2017-12-21T04:45:02.450Z"
            },
            {
                "_id": "5ab3775f35bf83edaa7bf273",
                "id": "UHJvamVjdDo1YWIzNzc1ZjM1YmY4M2VkYWE3YmYyNzM=",
                "name": "NetAppChatBot",
                "desc": "A ChatBot to identify the product",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Mar-22-2018 12:16:33."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "cena"
                },
                "updatedAt": "2018-03-22T09:29:38.826Z"
            },
            {
                "_id": "5ab376d735bf83edaa7bdc05",
                "id": "UHJvamVjdDo1YWIzNzZkNzM1YmY4M2VkYWE3YmRjMDU=",
                "name": "wolseley6",
                "desc": "Ferguson",
                "ner": {
                    "status": "training_failed",
                    "status_message": "Atleast 2 custom entities are mandatory to perform entity training. Please add one more custom entity to proceed."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "cena"
                },
                "updatedAt": "2018-03-22T09:26:55.660Z"
            },
            {
                "_id": "5ab3778e35bf83edaa7bfecd",
                "id": "UHJvamVjdDo1YWIzNzc4ZTM1YmY4M2VkYWE3YmZlY2Q=",
                "name": "Yourhanes",
                "desc": "Hanes shopping assistant",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Mar-22-2018 12:21:08."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "cena"
                },
                "updatedAt": "2018-03-22T09:30:48.522Z"
            },
            {
                "_id": "5ab376b735bf83edaa7bdbf1",
                "id": "UHJvamVjdDo1YWIzNzZiNzM1YmY4M2VkYWE3YmRiZjE=",
                "name": "rajeev1",
                "desc": "8200 model",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Mar-22-2018 12:31:05."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "cena"
                },
                "updatedAt": "2018-03-22T09:27:02.201Z"
            },
            {
                "_id": "5ab4d8a9c9b8e8bacbcd5898",
                "id": "UHJvamVjdDo1YWI0ZDhhOWM5YjhlOGJhY2JjZDU4OTg=",
                "name": "WalMart",
                "desc": "WalMart Bot",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jun-04-2018 05:17:14."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-03-23T10:37:16.938Z"
            },
            {
                "_id": "5ab8cbb1c9b8e8bacbd2a41a",
                "id": "UHJvamVjdDo1YWI4Y2JiMWM5YjhlOGJhY2JkMmE0MWE=",
                "name": "HEBDescription",
                "desc": "HEBDescription",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "innovationservices"
                },
                "updatedAt": "2018-03-26T10:31:12.978Z"
            },
            {
                "_id": "5ac8d1817d8ffd48937232e8",
                "id": "UHJvamVjdDo1YWM4ZDE4MTdkOGZmZDQ4OTM3MjMyZTg=",
                "name": "testboots1",
                "desc": "testboots1",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "innovationservices"
                },
                "updatedAt": "2018-04-07T14:11:15.275Z"
            },
            {
                "_id": "5a3a5d0b4e0d07801047b14d",
                "id": "UHJvamVjdDo1YTNhNWQwYjRlMGQwNzgwMTA0N2IxNGQ=",
                "name": "Walters-Kluer-Problem-Resolution",
                "desc": "Walters-Kluer-Problem-Resolution ",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Dec-21-2017 12:36:25."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-12-20T12:52:55.391Z"
            },
            {
                "_id": "5a8ba43627aacd44ab126844",
                "id": "UHJvamVjdDo1YThiYTQzNjI3YWFjZDQ0YWIxMjY4NDQ=",
                "name": "InteractionDemo",
                "desc": "preparing interaction model",
                "ner": {
                    "status": "trained",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "keshav"
                },
                "updatedAt": "2018-02-20T04:31:19.608Z"
            },
            {
                "_id": "5ab4d251c9b8e8bacbcd2069",
                "id": "UHJvamVjdDo1YWI0ZDI1MWM5YjhlOGJhY2JjZDIwNjk=",
                "name": "FergusonBot",
                "desc": "ferguson Sales Bot",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Mar-23-2018 10:50:07."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "cena"
                },
                "updatedAt": "2018-03-23T10:09:39.491Z"
            },
            {
                "_id": "5add9fba460bbd27ed807b06",
                "id": "UHJvamVjdDo1YWRkOWZiYTQ2MGJiZDI3ZWQ4MDdiMDY=",
                "name": "sample",
                "desc": "learning purpose",
                "ner": {
                    "status": "trained",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-04-23T08:56:41.910Z"
            },
            {
                "_id": "5adeb655460bbd27ed820b44",
                "id": "UHJvamVjdDo1YWRlYjY1NTQ2MGJiZDI3ZWQ4MjBiNDQ=",
                "name": "AlexaIce",
                "desc": "Integration of Alexa with ICE XD ",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "LizGeorge"
                },
                "updatedAt": "2018-04-24T04:45:11.093Z"
            },
            {
                "_id": "5b0ee3eb003fe4047446a739",
                "id": "UHJvamVjdDo1YjBlZTNlYjAwM2ZlNDA0NzQ0NmE3Mzk=",
                "name": "HRSAssessment",
                "desc": "HRSAssessment",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "smart"
                },
                "updatedAt": "2018-05-30T21:14:19.127Z"
            },
            {
                "_id": "5b14e059003fe4047459a1fb",
                "id": "UHJvamVjdDo1YjE0ZTA1OTAwM2ZlNDA0NzQ1OWExZmI=",
                "name": "netapp-onproduction",
                "desc": "Netapp",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jun-28-2018 00:12:51."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "netapp"
                },
                "updatedAt": "2018-06-04T06:46:55.494Z"
            },
            {
                "_id": "5ba4dcdf9667f708d2c2958e",
                "id": "UHJvamVjdDo1YmE0ZGNkZjk2NjdmNzA4ZDJjMjk1OGU=",
                "name": "Usecase1",
                "desc": "Usecase1",
                "ner": {
                    "status": "training_failed",
                    "status_message": "Unable to do entity training as no custom entities are mapped. Please map atleast 2 custom entities to proceed."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "innovationservices"
                },
                "updatedAt": "2018-09-21T11:58:37.637Z"
            },
            {
                "_id": "5a13fed631121f93b725b7a2",
                "id": "UHJvamVjdDo1YTEzZmVkNjMxMTIxZjkzYjcyNWI3YTI=",
                "name": "mailtest",
                "desc": "mailtest",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Nov-21-2017 10:28:38."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-11-21T10:24:38.909Z"
            },
            {
                "_id": "5a18116f31121f93b7286e24",
                "id": "UHJvamVjdDo1YTE4MTE2ZjMxMTIxZjkzYjcyODZlMjQ=",
                "name": "eeq",
                "desc": "qwqwe",
                "ner": {
                    "status": "trained",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-11-24T12:33:01.477Z"
            },
            {
                "_id": "5a26271f31121f93b72dc8cf",
                "id": "UHJvamVjdDo1YTI2MjcxZjMxMTIxZjkzYjcyZGM4Y2Y=",
                "name": "justtesting",
                "desc": "just testing",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Dec-05-2017 12:18:45."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-12-05T04:57:27.883Z"
            },
            {
                "_id": "5a584b2846b5b87be7ef63fd",
                "id": "UHJvamVjdDo1YTU4NGIyODQ2YjViODdiZTdlZjYzZmQ=",
                "name": "WK-Digital",
                "desc": "WK-Digital",
                "ner": {
                    "status": "trained",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2018-01-12T05:44:23.360Z"
            },
            {
                "_id": "5a702ac127aacd44abce2b0e",
                "id": "UHJvamVjdDo1YTcwMmFjMTI3YWFjZDQ0YWJjZTJiMGU=",
                "name": "UPSDemo",
                "desc": "UPSDemo",
                "ner": {
                    "status": "trained",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "trained",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2018-01-30T08:20:17.093Z"
            },
            {
                "_id": "5a7d45c827aacd44abeb6e69",
                "id": "UHJvamVjdDo1YTdkNDVjODI3YWFjZDQ0YWJlYjZlNjk=",
                "name": "Costco-category",
                "desc": "Identify costco product category, brand and product",
                "ner": {
                    "status": "trained",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "trained",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "smitha"
                },
                "updatedAt": "2018-02-09T06:55:04.350Z"
            },
            {
                "_id": "5a850ae427aacd44ab0049e8",
                "id": "UHJvamVjdDo1YTg1MGFlNDI3YWFjZDQ0YWIwMDQ5ZTg=",
                "name": "Pizza",
                "desc": "To order a pizza",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Feb-15-2018 04:39:08."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-02-15T04:23:20.848Z"
            },
            {
                "_id": "5a966f8427aacd44ab2f1319",
                "id": "UHJvamVjdDo1YTk2NmY4NDI3YWFjZDQ0YWIyZjEzMTk=",
                "name": "testimport",
                "desc": "testimport",
                "ner": {
                    "status": "trained",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "trained",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2018-02-28T09:00:14.922Z"
            },
            {
                "_id": "5a96703927aacd44ab2fbae1",
                "id": "UHJvamVjdDo1YTk2NzAzOTI3YWFjZDQ0YWIyZmJhZTE=",
                "name": "testboots",
                "desc": "testboots",
                "ner": {
                    "status": "trained",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2018-02-28T09:02:51.347Z"
            },
            {
                "_id": "5ab36e0635bf83edaa7ac67a",
                "id": "UHJvamVjdDo1YWIzNmUwNjM1YmY4M2VkYWE3YWM2N2E=",
                "name": "Wolseleydemo1",
                "desc": "Wolseley - Ferguson chatbot",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "cena"
                },
                "updatedAt": "2018-03-22T08:54:53.260Z"
            },
            {
                "_id": "59f96b85df0d8943fc6cef62",
                "id": "UHJvamVjdDo1OWY5NmI4NWRmMGQ4OTQzZmM2Y2VmNjI=",
                "name": "testForDemo",
                "desc": "sample for testing",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Mar-23-2018 09:38:45."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-11-01T06:37:10.030Z"
            },
            {
                "_id": "5af27bb121b1df0d64615ce9",
                "id": "UHJvamVjdDo1YWYyN2JiMTIxYjFkZjBkNjQ2MTVjZTk=",
                "name": "train2",
                "desc": "A bot to train",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-05-09T05:00:13.839Z"
            },
            {
                "_id": "5b15074f003fe404745b79a0",
                "id": "UHJvamVjdDo1YjE1MDc0ZjAwM2ZlNDA0NzQ1Yjc5YTA=",
                "name": "Maersk-bot",
                "desc": "Tracking Shipments",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-06-04T09:33:13.802Z"
            },
            {
                "_id": "5ae987979092520a8884aab3",
                "id": "UHJvamVjdDo1YWU5ODc5NzkwOTI1MjBhODg4NGFhYjM=",
                "name": "ggg",
                "desc": "a api test",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on May-02-2018 09:46:58."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-05-02T09:40:49.302Z"
            },
            {
                "_id": "5c57caa66e08183753fa25f8",
                "id": "UHJvamVjdDo1YzU3Y2FhNjZlMDgxODM3NTNmYTI1Zjg=",
                "name": "testqwe",
                "desc": "test123",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-02-04T05:16:23.956Z"
            },
            {
                "_id": "5c57fe736e0818375301ad8d",
                "id": "UHJvamVjdDo1YzU3ZmU3MzZlMDgxODM3NTMwMWFkOGQ=",
                "name": "testxxxxxx",
                "desc": "xxxxxxxxxxx",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-02-04T09:24:56.974Z"
            },
            {
                "_id": "5c5815156e0818375305892d",
                "id": "UHJvamVjdDo1YzU4MTUxNTZlMDgxODM3NTMwNTg5MmQ=",
                "name": "admin",
                "desc": "admin@1234",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "icetest"
                },
                "updatedAt": "2019-02-04T10:39:25.276Z"
            },
            {
                "_id": "5c58154f6e08183753059cc3",
                "id": "UHJvamVjdDo1YzU4MTU0ZjZlMDgxODM3NTMwNTljYzM=",
                "name": "testvishnu",
                "desc": "vishnurajkv",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-02-04T10:37:03.223Z"
            },
            {
                "_id": "5ac5c50738ee5ee2f5bb54a1",
                "id": "UHJvamVjdDo1YWM1YzUwNzM4ZWU1ZWUyZjViYjU0YTE=",
                "name": "BootsSalesOrderDemo",
                "desc": "Copy of boots sales order",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Apr-05-2018 06:43:00."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "unni"
                },
                "updatedAt": "2018-04-05T06:41:12.472Z"
            },
            {
                "_id": "5ac62c417d8ffd48936d13af",
                "id": "UHJvamVjdDo1YWM2MmM0MTdkOGZmZDQ4OTM2ZDEzYWY=",
                "name": "qwer",
                "desc": "A demo bot",
                "ner": {
                    "status": "trained",
                    "status_message": "Atleast 2 custom entities are mandatory to perform entity training. Please add one more custom entity to proceed."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-04-05T14:01:48.198Z"
            },
            {
                "_id": "5acafc807d8ffd4893778823",
                "id": "UHJvamVjdDo1YWNhZmM4MDdkOGZmZDQ4OTM3Nzg4MjM=",
                "name": "INSURANCEASSISTANT",
                "desc": "An insurance assistant that directly interacts with user",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jun-04-2018 05:19:39."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-04-09T05:39:21.220Z"
            },
            {
                "_id": "5a17a77a31121f93b727b1cc",
                "id": "UHJvamVjdDo1YTE3YTc3YTMxMTIxZjkzYjcyN2IxY2M=",
                "name": "Appstate",
                "desc": "checking for application status",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Dec-11-2017 05:34:02."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-11-24T05:05:10.374Z"
            },
            {
                "_id": "5a31f8cefba8195fe960b61d",
                "id": "UHJvamVjdDo1YTMxZjhjZWZiYTgxOTVmZTk2MGI2MWQ=",
                "name": "state-street-test1",
                "desc": "Created for state street test in new UI",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Dec-28-2017 10:00:02."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-12-14T04:07:07.369Z"
            },
            {
                "_id": "5aced201460bbd27ed6e20fd",
                "id": "UHJvamVjdDo1YWNlZDIwMTQ2MGJiZDI3ZWQ2ZTIwZmQ=",
                "name": "ASDAvoicebot",
                "desc": "A voice bot for ASDA",
                "ner": {
                    "status": "trained",
                    "status_message": "Unable to do entity training as no custom entities are mapped. Please map atleast 2 custom entities to proceed."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-04-12T03:27:35.047Z"
            },
            {
                "_id": "5acee75c460bbd27ed6ed61b",
                "id": "UHJvamVjdDo1YWNlZTc1YzQ2MGJiZDI3ZWQ2ZWQ2MWI=",
                "name": "Vanguard",
                "desc": "A bot for vanguard",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jun-04-2018 05:09:25."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-04-12T04:58:13.197Z"
            },
            {
                "_id": "5acf08a1460bbd27ed6f053a",
                "id": "UHJvamVjdDo1YWNmMDhhMTQ2MGJiZDI3ZWQ2ZjA1M2E=",
                "name": "vanguardcharitable",
                "desc": "Bot for vanguard charitable",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jun-04-2018 05:16:25."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-04-12T07:21:25.693Z"
            },
            {
                "_id": "5acf2281460bbd27ed6f1e3e",
                "id": "UHJvamVjdDo1YWNmMjI4MTQ2MGJiZDI3ZWQ2ZjFlM2U=",
                "name": "ASDAVOICEBOT2",
                "desc": "Updated voice bot for ASDA",
                "ner": {
                    "status": "trained",
                    "status_message": "Unable to do entity training as no custom entities are mapped. Please map atleast 2 custom entities to proceed."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-04-12T09:10:42.438Z"
            },
            {
                "_id": "5ad6d883460bbd27ed769a51",
                "id": "UHJvamVjdDo1YWQ2ZDg4MzQ2MGJiZDI3ZWQ3NjlhNTE=",
                "name": "ATMASSISTANT",
                "desc": "An ATM assistant",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jun-04-2018 05:36:50."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-04-18T05:32:59.426Z"
            },
            {
                "_id": "5ad6e036460bbd27ed76c328",
                "id": "UHJvamVjdDo1YWQ2ZTAzNjQ2MGJiZDI3ZWQ3NmMzMjg=",
                "name": "REFERALASSISTANT",
                "desc": "A bot for medical reference",
                "ner": {
                    "status": "new",
                    "status_message": "Entity recognition model published successfully on Jun-04-2018 06:48:39."
                },
                "ir": {
                    "status": "new",
                    "status_message": "Intent recognition model published successfully on Jun-04-2018 06:48:36."
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-04-18T06:05:54.321Z"
            },
            {
                "_id": "5ad6e92a460bbd27ed76e775",
                "id": "UHJvamVjdDo1YWQ2ZTkyYTQ2MGJiZDI3ZWQ3NmU3NzU=",
                "name": "TROUBLESHOOTERASST",
                "desc": "A bot to trouble shoot",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Apr-18-2018 07:14:36."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-04-18T06:44:10.439Z"
            },
            {
                "_id": "5ad96d7a460bbd27ed7b3ad5",
                "id": "UHJvamVjdDo1YWQ5NmQ3YTQ2MGJiZDI3ZWQ3YjNhZDU=",
                "name": "RETAILASST",
                "desc": "A bot for food delivery",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on May-07-2018 05:07:50."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-04-20T04:33:08.022Z"
            },
            {
                "_id": "5ad9910a460bbd27ed7c6d02",
                "id": "UHJvamVjdDo1YWQ5OTEwYTQ2MGJiZDI3ZWQ3YzZkMDI=",
                "name": "FINANACIALASST",
                "desc": "Bot provides finanacial services",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Apr-20-2018 07:17:10."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-04-20T07:05:16.614Z"
            },
            {
                "_id": "5add988e460bbd27ed8041f3",
                "id": "UHJvamVjdDo1YWRkOTg4ZTQ2MGJiZDI3ZWQ4MDQxZjM=",
                "name": "demobot",
                "desc": "a simple demo bot",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on May-08-2018 11:26:21."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-04-23T08:26:02.920Z"
            },
            {
                "_id": "5ae07272460bbd27ed833422",
                "id": "UHJvamVjdDo1YWUwNzI3MjQ2MGJiZDI3ZWQ4MzM0MjI=",
                "name": "KGDemoIBMSpectrum",
                "desc": "Demo for KG IBM Spectrum Scale",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "innovationservices"
                },
                "updatedAt": "2018-04-25T12:21:09.021Z"
            },
            {
                "_id": "5ae0c3d9460bbd27ed83b115",
                "id": "UHJvamVjdDo1YWUwYzNkOTQ2MGJiZDI3ZWQ4M2IxMTU=",
                "name": "RPABluePrism",
                "desc": "BluePrismUseCase",
                "ner": {
                    "status": "training_failed",
                    "status_message": "Atleast 2 custom entities are mandatory to perform entity training. Please add one more custom entity to proceed."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "innovationservices"
                },
                "updatedAt": "2018-04-25T18:07:43.114Z"
            },
            {
                "_id": "5ae0ca9c460bbd27ed83ed07",
                "id": "UHJvamVjdDo1YWUwY2E5YzQ2MGJiZDI3ZWQ4M2VkMDc=",
                "name": "BPProject",
                "desc": "BluePrismProject",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Apr-25-2018 18:54:22."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "innovationservices"
                },
                "updatedAt": "2018-04-25T18:36:20.144Z"
            },
            {
                "_id": "5ae2e34c460bbd27ed8610cd",
                "id": "UHJvamVjdDo1YWUyZTM0YzQ2MGJiZDI3ZWQ4NjEwY2Q=",
                "name": "IBCCXAAnalysis",
                "desc": "ChatBot forIBC CXA Analysis",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "innovationservices"
                },
                "updatedAt": "2018-04-27T08:46:08.744Z"
            },
            {
                "_id": "5ae94e8a9092520a88845a4f",
                "id": "UHJvamVjdDo1YWU5NGU4YTkwOTI1MjBhODg4NDVhNGY=",
                "name": "Infinityknowledge",
                "desc": "infinity knowledge repository",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on May-02-2018 05:48:12."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-05-02T05:38:03.742Z"
            },
            {
                "_id": "5ae99dea9092520a8884e1a1",
                "id": "UHJvamVjdDo1YWU5OWRlYTkwOTI1MjBhODg4NGUxYTE=",
                "name": "anthemtest",
                "desc": "test of anthem",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on May-03-2018 10:31:34."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "engineering"
                },
                "updatedAt": "2018-05-02T11:15:55.986Z"
            },
            {
                "_id": "5aea90559092520a888561da",
                "id": "UHJvamVjdDo1YWVhOTA1NTkwOTI1MjBhODg4NTYxZGE=",
                "name": "SIPSolution",
                "desc": "SIP phone solution",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-02-04T07:11:48.423Z"
            },
            {
                "_id": "5ad9b180460bbd27ed7c7f1d",
                "id": "UHJvamVjdDo1YWQ5YjE4MDQ2MGJiZDI3ZWQ3YzdmMWQ=",
                "name": "SHOPPINGASST",
                "desc": "A buddy on shopping",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on May-04-2018 04:59:59."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-04-20T09:24:09.036Z"
            },
            {
                "_id": "5af0072921b1df0d645cba61",
                "id": "UHJvamVjdDo1YWYwMDcyOTIxYjFkZjBkNjQ1Y2JhNjE=",
                "name": "pdfExtraction",
                "desc": "pdfExtraction",
                "ner": {
                    "status": "training_failed",
                    "status_message": "Unable to do entity training as no custom entities are mapped. Please map atleast 2 custom entities to proceed."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2018-05-07T07:58:46.977Z"
            },
            {
                "_id": "5af1827121b1df0d645fdfe3",
                "id": "UHJvamVjdDo1YWYxODI3MTIxYjFkZjBkNjQ1ZmRmZTM=",
                "name": "train",
                "desc": "a bot",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on May-08-2018 13:52:28."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-05-08T10:56:58.973Z"
            },
            {
                "_id": "5af2ca6321b1df0d64632bf6",
                "id": "UHJvamVjdDo1YWYyY2E2MzIxYjFkZjBkNjQ2MzJiZjY=",
                "name": "hhhh",
                "desc": "healthcare bot",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on May-09-2018 10:45:12."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-05-09T10:16:09.811Z"
            },
            {
                "_id": "5af29b1d21b1df0d6461e918",
                "id": "UHJvamVjdDo1YWYyOWIxZDIxYjFkZjBkNjQ2MWU5MTg=",
                "name": "deby",
                "desc": "debychat",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on May-10-2018 06:19:01."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-05-09T06:54:40.846Z"
            },
            {
                "_id": "5af3d25e21b1df0d6464cacf",
                "id": "UHJvamVjdDo1YWYzZDI1ZTIxYjFkZjBkNjQ2NGNhY2Y=",
                "name": "ticket",
                "desc": "ticket raising",
                "ner": {
                    "status": "trained",
                    "status_message": "Unable to do entity training as no custom entities are mapped. Please map atleast 2 custom entities to proceed."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-05-10T05:02:32.756Z"
            },
            {
                "_id": "5af40b1b21b1df0d646599c9",
                "id": "UHJvamVjdDo1YWY0MGIxYjIxYjFkZjBkNjQ2NTk5Yzk=",
                "name": "Next",
                "desc": "Next usecase",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on May-10-2018 11:25:52."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-05-10T09:04:40.212Z"
            },
            {
                "_id": "5af4387b21b1df0d646648c3",
                "id": "UHJvamVjdDo1YWY0Mzg3YjIxYjFkZjBkNjQ2NjQ4YzM=",
                "name": "incidentraising",
                "desc": "ticketraising",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on May-10-2018 12:30:24."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-05-10T12:18:10.051Z"
            },
            {
                "_id": "5af51c1221b1df0d6476b20a",
                "id": "UHJvamVjdDo1YWY1MWMxMjIxYjFkZjBkNjQ3NmIyMGE=",
                "name": "demostudy",
                "desc": "a bot for demo",
                "ner": {
                    "status": "trained",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-05-11T04:29:24.745Z"
            },
            {
                "_id": "5af51d0721b1df0d6476bd7d",
                "id": "UHJvamVjdDo1YWY1MWQwNzIxYjFkZjBkNjQ3NmJkN2Q=",
                "name": "AmishiD",
                "desc": "Test Wol",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on May-11-2018 07:27:35."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "europe"
                },
                "updatedAt": "2018-05-11T04:33:20.881Z"
            },
            {
                "_id": "5b07c2fb0e8e769cc4478088",
                "id": "UHJvamVjdDo1YjA3YzJmYjBlOGU3NjljYzQ0NzgwODg=",
                "name": "TestProject",
                "desc": "TestProjectstudy",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on May-28-2018 05:03:59."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "innovationservices"
                },
                "updatedAt": "2018-05-25T08:02:13.481Z"
            },
            {
                "_id": "5b0cfc130e8e769cc44e4d66",
                "id": "UHJvamVjdDo1YjBjZmMxMzBlOGU3NjljYzQ0ZTRkNjY=",
                "name": "LocationIdentifier",
                "desc": "Location Identifier",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on May-29-2018 10:38:44."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2018-05-29T10:27:43.825Z"
            },
            {
                "_id": "5b0fcbad003fe404744f5fea",
                "id": "UHJvamVjdDo1YjBmY2JhZDAwM2ZlNDA0NzQ0ZjVmZWE=",
                "name": "UseCase2-Script",
                "desc": "Tax Consultancy",
                "ner": {
                    "status": "trained",
                    "status_message": "Unable to do entity training as no custom entities are mapped. Please map atleast 2 custom entities to proceed."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-05-31T11:13:52.142Z"
            },
            {
                "_id": "5b0fc9e2003fe404744f3945",
                "id": "UHJvamVjdDo1YjBmYzllMjAwM2ZlNDA0NzQ0ZjM5NDU=",
                "name": "SampleProjectPrinter",
                "desc": "Use Case 1 New User (Printer)",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jun-04-2018 10:16:56."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-05-31T11:15:37.465Z"
            },
            {
                "_id": "5b14ca6b003fe40474578fed",
                "id": "UHJvamVjdDo1YjE0Y2E2YjAwM2ZlNDA0NzQ1NzhmZWQ=",
                "name": "EquifaxInc-Bot",
                "desc": "Credit Card Report",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jun-13-2018 08:39:41."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-06-04T05:13:23.367Z"
            },
            {
                "_id": "5ac4ac5138ee5ee2f5b90b59",
                "id": "UHJvamVjdDo1YWM0YWM1MTM4ZWU1ZWUyZjViOTBiNTk=",
                "name": "Nissan",
                "desc": "Nissan car Service bot",
                "ner": {
                    "status": "trained",
                    "status_message": "Unable to do entity training as no custom entities are mapped. Please map atleast 2 custom entities to proceed."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-04-04T10:43:46.420Z"
            },
            {
                "_id": "5b1601dc003fe404745ff082",
                "id": "UHJvamVjdDo1YjE2MDFkYzAwM2ZlNDA0NzQ1ZmYwODI=",
                "name": "SampleSkillSearch",
                "desc": "Chat bot to search for job matching skills",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jun-08-2018 09:01:43."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "u35350"
                },
                "updatedAt": "2018-06-05T03:22:19.356Z"
            },
            {
                "_id": "5b1a231b003fe404747309cf",
                "id": "UHJvamVjdDo1YjFhMjMxYjAwM2ZlNDA0NzQ3MzA5Y2Y=",
                "name": "retailusecase123",
                "desc": "retailusecase",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jun-25-2018 06:43:02."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-06-08T06:33:02.460Z"
            },
            {
                "_id": "5b1df7fee918780a05a9ba6d",
                "id": "UHJvamVjdDo1YjFkZjdmZWU5MTg3ODBhMDVhOWJhNmQ=",
                "name": "HRBot",
                "desc": "HR bot for answering job  related queries",
                "ner": {
                    "status": "trained",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "walmart"
                },
                "updatedAt": "2018-06-11T04:25:48.585Z"
            },
            {
                "_id": "5b1df9d7e918780a05aa29f4",
                "id": "UHJvamVjdDo1YjFkZjlkN2U5MTg3ODBhMDVhYTI5ZjQ=",
                "name": "MychatApp",
                "desc": "Leanring Application",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jun-11-2018 05:28:39."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "walmart"
                },
                "updatedAt": "2018-06-11T04:27:15.464Z"
            },
            {
                "_id": "5b1dfe21e918780a05aa900b",
                "id": "UHJvamVjdDo1YjFkZmUyMWU5MTg3ODBhMDVhYTkwMGI=",
                "name": "Skv123",
                "desc": "sample xyz",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jun-11-2018 06:06:34."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "walmart"
                },
                "updatedAt": "2018-06-11T04:44:44.755Z"
            },
            {
                "_id": "5b1df868e918780a05a9c0b1",
                "id": "UHJvamVjdDo1YjFkZjg2OGU5MTg3ODBhMDVhOWMwYjE=",
                "name": "TravelBooking",
                "desc": "A chat bot to trip ",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jun-11-2018 05:52:40."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "walmart"
                },
                "updatedAt": "2018-06-11T04:25:49.632Z"
            },
            {
                "_id": "5b1df9dee918780a05aa2a03",
                "id": "UHJvamVjdDo1YjFkZjlkZWU5MTg3ODBhMDVhYTJhMDM=",
                "name": "hrchatbot",
                "desc": "chatboy for HR",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jun-11-2018 06:24:32."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "walmart"
                },
                "updatedAt": "2018-06-11T04:27:02.195Z"
            },
            {
                "_id": "5b1e0bf7e918780a05ab27c8",
                "id": "UHJvamVjdDo1YjFlMGJmN2U5MTg3ODBhMDVhYjI3Yzg=",
                "name": "bookMyShow",
                "desc": "helps to users to book the movie ticket online",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "walmart"
                },
                "updatedAt": "2018-06-11T05:43:19.726Z"
            },
            {
                "_id": "5b1dfb82e918780a05aa4b25",
                "id": "UHJvamVjdDo1YjFkZmI4MmU5MTg3ODBhMDVhYTRiMjU=",
                "name": "sampledemo",
                "desc": "chatbot for  retail store walmart",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Aug-13-2018 10:07:46."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "walmart"
                },
                "updatedAt": "2018-08-10T06:39:00.548Z"
            },
            {
                "_id": "5b1e36b1e918780a05ae2dd8",
                "id": "UHJvamVjdDo1YjFlMzZiMWU5MTg3ODBhMDVhZTJkZDg=",
                "name": "LoanCalcBot",
                "desc": "Chat bot for getting the loan details",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jun-14-2018 04:07:04."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "walmart"
                },
                "updatedAt": "2018-06-11T08:45:46.814Z"
            },
            {
                "_id": "5b1fa629e918780a05b248e6",
                "id": "UHJvamVjdDo1YjFmYTYyOWU5MTg3ODBhMDViMjQ4ZTY=",
                "name": "POCChatbot",
                "desc": "Chatbot to provide user id corresponding to the given id",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jun-28-2018 08:58:01."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "innovationservices"
                },
                "updatedAt": "2018-06-12T10:54:55.064Z"
            },
            {
                "_id": "5a68b82327aacd44abc88c8d",
                "id": "UHJvamVjdDo1YTY4YjgyMzI3YWFjZDQ0YWJjODhjOGQ=",
                "name": "AsstForDiscover",
                "desc": "AsstForDiscover - Demo",
                "ner": {
                    "status": "trained",
                    "status_message": "Atleast 2 custom entities are mandatory to perform entity training. Please add one more custom entity to proceed."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "deepa"
                },
                "updatedAt": "2018-01-24T16:45:34.090Z"
            },
            {
                "_id": "5b30723bd15aba2c9d46caef",
                "id": "UHJvamVjdDo1YjMwNzIzYmQxNWFiYTJjOWQ0NmNhZWY=",
                "name": "kochitest",
                "desc": "demo for kochi team",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jun-25-2018 05:10:20."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-06-25T04:41:19.333Z"
            },
            {
                "_id": "5b30725fd15aba2c9d46cb03",
                "id": "UHJvamVjdDo1YjMwNzI1ZmQxNWFiYTJjOWQ0NmNiMDM=",
                "name": "princessbot",
                "desc": "Chat bot for princess.com",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jun-25-2018 07:27:43."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "ilkochi"
                },
                "updatedAt": "2018-06-25T04:41:54.424Z"
            },
            {
                "_id": "5b3476a935b90f0977445b6c",
                "id": "UHJvamVjdDo1YjM0NzZhOTM1YjkwZjA5Nzc0NDViNmM=",
                "name": "Netapp-Quoteedge",
                "desc": "Net app QuoteEdge",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "netapp"
                },
                "updatedAt": "2018-06-28T05:48:40.936Z"
            },
            {
                "_id": "595b5d1bc9c57fd148d08900",
                "id": "UHJvamVjdDo1OTViNWQxYmM5YzU3ZmQxNDhkMDg5MDA=",
                "name": "Greeting",
                "desc": "Greetings identification",
                "ner": {
                    "status": "training_failed",
                    "status_message": "Token mapping missing from training data"
                },
                "ir": {
                    "status": "training_failed",
                    "status_message": "expected string or buffer"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-07-04T09:18:13.361Z"
            },
            {
                "_id": "5b443e164374de092df8ef1a",
                "id": "UHJvamVjdDo1YjQ0M2UxNjQzNzRkZTA5MmRmOGVmMWE=",
                "name": "test-10",
                "desc": "test project",
                "ner": {
                    "status": "training_failed",
                    "status_message": "Unable to do entity training as no custom entities are mapped. Please map atleast 2 custom entities to proceed."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "sreejith"
                },
                "updatedAt": "2018-07-10T05:07:35.834Z"
            },
            {
                "_id": "5b4593ecdae133096329ad10",
                "id": "UHJvamVjdDo1YjQ1OTNlY2RhZTEzMzA5NjMyOWFkMTA=",
                "name": "boots-test",
                "desc": "Boots test cases",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jul-16-2018 08:44:08."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "smitha"
                },
                "updatedAt": "2018-07-11T05:21:49.121Z"
            },
            {
                "_id": "5b4c5e9cc9a9b809e1378b2e",
                "id": "UHJvamVjdDo1YjRjNWU5Y2M5YTliODA5ZTEzNzhiMmU=",
                "name": "BootsProducts",
                "desc": "BootsProducts",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "smart"
                },
                "updatedAt": "2018-07-16T09:01:16.422Z"
            },
            {
                "_id": "5b55651ac9a9b809e1412e3a",
                "id": "UHJvamVjdDo1YjU1NjUxYWM5YTliODA5ZTE0MTJlM2E=",
                "name": "Anoop-Test",
                "desc": "Test project created for Anoop",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jul-23-2018 05:55:05."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "smitha"
                },
                "updatedAt": "2018-07-23T07:02:08.429Z"
            },
            {
                "_id": "5b55a419c9a9b809e143fe97",
                "id": "UHJvamVjdDo1YjU1YTQxOWM5YTliODA5ZTE0M2ZlOTc=",
                "name": "MessageIndicator",
                "desc": " categorize the server providing message",
                "ner": {
                    "status": "training_failed",
                    "status_message": "Unable to do entity training as no custom entities are mapped. Please map atleast 2 custom entities to proceed."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "walmart"
                },
                "updatedAt": "2018-07-23T09:47:12.614Z"
            },
            {
                "_id": "5b55afe4c9a9b809e1452dc0",
                "id": "UHJvamVjdDo1YjU1YWZlNGM5YTliODA5ZTE0NTJkYzA=",
                "name": "MessageSeverityCalculator",
                "desc": "Message Severity Calculator",
                "ner": {
                    "status": "trained",
                    "status_message": "Unable to do entity training as no custom entities are mapped. Please map atleast 2 custom entities to proceed."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "walmart"
                },
                "updatedAt": "2018-07-23T10:37:34.107Z"
            },
            {
                "_id": "5b55bfbac9a9b809e1476d95",
                "id": "UHJvamVjdDo1YjU1YmZiYWM5YTliODA5ZTE0NzZkOTU=",
                "name": "TestResetPassword",
                "desc": "resetpassword",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jul-23-2018 11:49:39."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "innovationservices"
                },
                "updatedAt": "2018-07-23T11:46:57.186Z"
            },
            {
                "_id": "5b55c2b9c9a9b809e147f9e5",
                "id": "UHJvamVjdDo1YjU1YzJiOWM5YTliODA5ZTE0N2Y5ZTU=",
                "name": "UserValidationPOC",
                "desc": "get user id and pin and validate it and send mail",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jul-23-2018 12:01:25."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "innovationservices"
                },
                "updatedAt": "2018-07-23T11:58:10.505Z"
            },
            {
                "_id": "5b5a0236c9a9b809e1528fd3",
                "id": "UHJvamVjdDo1YjVhMDIzNmM5YTliODA5ZTE1MjhmZDM=",
                "name": "WBS-V0",
                "desc": "WBS-V0",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "smart"
                },
                "updatedAt": "2018-07-26T17:20:03.374Z"
            },
            {
                "_id": "5b61754b359c7f24178a2941",
                "id": "UHJvamVjdDo1YjYxNzU0YjM1OWM3ZjI0MTc4YTI5NDE=",
                "name": "AVA",
                "desc": "Anthem Virtual Assistance",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Aug-27-2018 05:00:27."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "sreejith"
                },
                "updatedAt": "2018-08-01T08:54:59.029Z"
            },
            {
                "_id": "5b6bf622359c7f241796858c",
                "id": "UHJvamVjdDo1YjZiZjYyMjM1OWM3ZjI0MTc5Njg1OGM=",
                "name": "Test-ava",
                "desc": "test-ava",
                "ner": {
                    "status": "trained",
                    "status_message": "Unable to do entity training as no custom entities are mapped. Please map atleast 2 custom entities to proceed."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "sreejith"
                },
                "updatedAt": "2018-08-09T08:07:11.716Z"
            },
            {
                "_id": "5b6d6b8b359c7f241798ce17",
                "id": "UHJvamVjdDo1YjZkNmI4YjM1OWM3ZjI0MTc5OGNlMTc=",
                "name": "VehiclePass",
                "desc": "training ",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Aug-10-2018 10:53:50."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "innovationservices"
                },
                "updatedAt": "2018-08-10T10:41:11.991Z"
            },
            {
                "_id": "5b6d76c3359c7f24179968ba",
                "id": "UHJvamVjdDo1YjZkNzZjMzM1OWM3ZjI0MTc5OTY4YmE=",
                "name": "LeaveRequest",
                "desc": "training",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Aug-10-2018 11:48:07."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "innovationservices"
                },
                "updatedAt": "2018-08-10T11:28:31.909Z"
            },
            {
                "_id": "5b861fa9359c7f2417c9c805",
                "id": "UHJvamVjdDo1Yjg2MWZhOTM1OWM3ZjI0MTdjOWM4MDU=",
                "name": "MedicalAssistant-septTest",
                "desc": "testing",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-02-04T09:26:15.919Z"
            },
            {
                "_id": "5b88cc41359c7f2417d364df",
                "id": "UHJvamVjdDo1Yjg4Y2M0MTM1OWM3ZjI0MTdkMzY0ZGY=",
                "name": "Sample",
                "desc": "Sample for learning",
                "ner": {
                    "status": "trained",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-08-31T05:04:06.146Z"
            },
            {
                "_id": "5b8fbe81359c7f2417e7cc40",
                "id": "UHJvamVjdDo1YjhmYmU4MTM1OWM3ZjI0MTdlN2NjNDA=",
                "name": "EquifaxPoc",
                "desc": "Equifax AppServerStart and Sftp server status check Poc",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Sep-05-2018 11:50:37."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "innovation"
                },
                "updatedAt": "2018-09-05T11:31:25.553Z"
            },
            {
                "_id": "5b978de9ee011d7ae1a6a93f",
                "id": "UHJvamVjdDo1Yjk3OGRlOWVlMDExZDdhZTFhNmE5M2Y=",
                "name": "FlightBookingSampleForKT",
                "desc": "FlightBookingSampleForKT",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "smart"
                },
                "updatedAt": "2018-09-11T09:42:01.190Z"
            },
            {
                "_id": "5ba0f5959667f708d2bc6595",
                "id": "UHJvamVjdDo1YmEwZjU5NTk2NjdmNzA4ZDJiYzY1OTU=",
                "name": "travelling",
                "desc": "testing",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Sep-19-2018 05:18:34."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-02-04T09:24:30.282Z"
            },
            {
                "_id": "5bb5e13dfc5bf10962417c18",
                "id": "UHJvamVjdDo1YmI1ZTEzZGZjNWJmMTA5NjI0MTdjMTg=",
                "name": "Sample-client",
                "desc": "Chat bot for client",
                "ner": {
                    "status": "trained",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-10-04T09:45:53.880Z"
            },
            {
                "_id": "5bbc62f9fc5bf10962469f59",
                "id": "UHJvamVjdDo1YmJjNjJmOWZjNWJmMTA5NjI0NjlmNTk=",
                "name": "Test-Vodafone",
                "desc": "Test-Vodafone",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Oct-09-2018 08:26:47."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2018-10-09T08:15:02.439Z"
            },
            {
                "_id": "5bbddf8ae516fe0a3be08bc5",
                "id": "UHJvamVjdDo1YmJkZGY4YWU1MTZmZTBhM2JlMDhiYzU=",
                "name": "NETAPP-ORIENTDB",
                "desc": "cz, testplans etc",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Oct-10-2018 12:09:04."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "netapp"
                },
                "updatedAt": "2018-10-10T11:16:31.042Z"
            },
            {
                "_id": "5bbeea90e516fe0a3be4a4cd",
                "id": "UHJvamVjdDo1YmJlZWE5MGU1MTZmZTBhM2JlNGE0Y2Q=",
                "name": "vodafoneorderrequest",
                "desc": "vodafone order request",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "innovationservices"
                },
                "updatedAt": "2018-10-11T10:06:32.012Z"
            },
            {
                "_id": "5bbeffafe516fe0a3be63bc9",
                "id": "UHJvamVjdDo1YmJlZmZhZmU1MTZmZTBhM2JlNjNiYzk=",
                "name": "netapp-test-cz-testplan",
                "desc": "cz, testplan",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "netapp"
                },
                "updatedAt": "2018-10-11T07:45:57.070Z"
            },
            {
                "_id": "5bbf2209e516fe0a3bf01a28",
                "id": "UHJvamVjdDo1YmJmMjIwOWU1MTZmZTBhM2JmMDFhMjg=",
                "name": "RajVodafone",
                "desc": "RajVodafone",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Oct-12-2018 05:11:27."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2018-10-12T05:26:03.015Z"
            },
            {
                "_id": "59f1675adf0d8943fc6b4c4e",
                "id": "UHJvamVjdDo1OWYxNjc1YWRmMGQ4OTQzZmM2YjRjNGU=",
                "name": "KG-Test",
                "desc": "NER for KG",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jun-22-2018 11:24:28."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-10-26T04:41:13.037Z"
            },
            {
                "_id": "59f96ba1df0d8943fc6cf641",
                "id": "UHJvamVjdDo1OWY5NmJhMWRmMGQ4OTQzZmM2Y2Y2NDE=",
                "name": "SreekanthcTest",
                "desc": "Testing project",
                "ner": {
                    "status": "trained",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-11-22T06:50:25.129Z"
            },
            {
                "_id": "59e83e56df0d8943fc69867d",
                "id": "UHJvamVjdDo1OWU4M2U1NmRmMGQ4OTQzZmM2OTg2N2Q=",
                "name": "testTravel",
                "desc": "testTravel",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Nov-10-2017 08:44:01."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-10-19T05:55:48.426Z"
            },
            {
                "_id": "5a3a24af66dc04cc378c76d6",
                "id": "UHJvamVjdDo1YTNhMjRhZjY2ZGMwNGNjMzc4Yzc2ZDY=",
                "name": "WaltersKluwer-KB",
                "desc": "Pleasde dont access this Project .",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Dec-21-2017 16:09:35."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-12-20T08:53:35.323Z"
            },
            {
                "_id": "5a5ee41327aacd44abb79b10",
                "id": "UHJvamVjdDo1YTVlZTQxMzI3YWFjZDQ0YWJiNzliMTA=",
                "name": "speechToText",
                "desc": "speechToText",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jan-17-2018 07:13:27."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2018-01-17T05:50:21.392Z"
            },
            {
                "_id": "5a74042327aacd44abd8e20a",
                "id": "UHJvamVjdDo1YTc0MDQyMzI3YWFjZDQ0YWJkOGUyMGE=",
                "name": "varunust",
                "desc": "Ust Trial",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Feb-02-2018 06:34:45."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-02-02T06:26:35.627Z"
            },
            {
                "_id": "5a83e21227aacd44abfd8ea7",
                "id": "UHJvamVjdDo1YTgzZTIxMjI3YWFjZDQ0YWJmZDhlYTc=",
                "name": "demozxc",
                "desc": "booking",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Feb-14-2018 07:23:33."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-02-14T07:15:52.360Z"
            },
            {
                "_id": "5ab3478335bf83edaa78b88c",
                "id": "UHJvamVjdDo1YWIzNDc4MzM1YmY4M2VkYWE3OGI4OGM=",
                "name": "testapp",
                "desc": "testapp",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Mar-22-2018 06:44:21."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "cena"
                },
                "updatedAt": "2018-03-22T06:05:30.130Z"
            },
            {
                "_id": "5b1df926e918780a05a9eb95",
                "id": "UHJvamVjdDo1YjFkZjkyNmU5MTg3ODBhMDVhOWViOTU=",
                "name": "TableBooking",
                "desc": "To book table in hotel",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jun-11-2018 06:00:39."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "walmart"
                },
                "updatedAt": "2018-06-11T04:26:12.083Z"
            },
            {
                "_id": "5b1fa65ce918780a05b24ca2",
                "id": "UHJvamVjdDo1YjFmYTY1Y2U5MTg3ODBhMDViMjRjYTI=",
                "name": "Sam",
                "desc": "Chatbot for getting   user id of the user.",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jul-03-2018 09:16:10."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "innovationservices"
                },
                "updatedAt": "2018-06-18T05:41:16.852Z"
            },
            {
                "_id": "5b07a1630e8e769cc44706ca",
                "id": "UHJvamVjdDo1YjA3YTE2MzBlOGU3NjljYzQ0NzA2Y2E=",
                "name": "Demo",
                "desc": "test and study",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on May-25-2018 05:59:16."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "innovationservices"
                },
                "updatedAt": "2018-05-25T05:41:03.388Z"
            },
            {
                "_id": "5bd2f522a973d070442b028b",
                "id": "UHJvamVjdDo1YmQyZjUyMmE5NzNkMDcwNDQyYjAyOGI=",
                "name": "Sempra-MCS-POC",
                "desc": "Sempra-MCS-POC",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "innovationtraining"
                },
                "updatedAt": "2018-10-26T11:06:11.784Z"
            },
            {
                "_id": "5bd823a5a973d0704433a7a6",
                "id": "UHJvamVjdDo1YmQ4MjNhNWE5NzNkMDcwNDQzM2E3YTY=",
                "name": "sample-newClient",
                "desc": "For a client meeting",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-10-30T09:25:58.201Z"
            },
            {
                "_id": "5be3d27335df3a6bd5c06c68",
                "id": "UHJvamVjdDo1YmUzZDI3MzM1ZGYzYTZiZDVjMDZjNjg=",
                "name": "Ashley-Alexa",
                "desc": "Alexa part for client",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-11-08T06:06:43.896Z"
            },
            {
                "_id": "5be3d4a835df3a6bd5c07c27",
                "id": "UHJvamVjdDo1YmUzZDRhODM1ZGYzYTZiZDVjMDdjMjc=",
                "name": "coffee",
                "desc": "Ashley Furniture -Demo",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-11-08T09:47:47.386Z"
            },
            {
                "_id": "5beaf0ed35df3a6bd5cdff4d",
                "id": "UHJvamVjdDo1YmVhZjBlZDM1ZGYzYTZiZDVjZGZmNGQ=",
                "name": "DemoAisleLocator",
                "desc": "DemoAisleLocator",
                "ner": {
                    "status": "training_failed",
                    "status_message": "Cannot have number of folds n_folds=3 greater than the number of samples: 2."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2018-11-13T15:42:38.963Z"
            },
            {
                "_id": "5bebeb4135df3a6bd5cfe054",
                "id": "UHJvamVjdDo1YmViZWI0MTM1ZGYzYTZiZDVjZmUwNTQ=",
                "name": "Marsh",
                "desc": "Marsh",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "innovationservices"
                },
                "updatedAt": "2018-11-14T09:30:43.868Z"
            },
            {
                "_id": "5bfbaefc35df3a6bd5f32882",
                "id": "UHJvamVjdDo1YmZiYWVmYzM1ZGYzYTZiZDVmMzI4ODI=",
                "name": "TestList",
                "desc": "TestList",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "smart"
                },
                "updatedAt": "2018-11-26T08:29:49.107Z"
            },
            {
                "_id": "5bfd10ac35df3a6bd5fb38f9",
                "id": "UHJvamVjdDo1YmZkMTBhYzM1ZGYzYTZiZDVmYjM4Zjk=",
                "name": "SocialExciteSentimentAnalysis",
                "desc": "configuring data for sentiment, category post type models",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "smart"
                },
                "updatedAt": "2018-11-27T09:38:52.836Z"
            },
            {
                "_id": "5c027b6b35df3a6bd5110f4d",
                "id": "UHJvamVjdDo1YzAyN2I2YjM1ZGYzYTZiZDUxMTBmNGQ=",
                "name": "healthcareproD3",
                "desc": "healthcareproD3",
                "ner": {
                    "status": "training_failed",
                    "status_message": "Not enough utterances for training"
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "sreejith"
                },
                "updatedAt": "2018-12-01T12:15:39.695Z"
            },
            {
                "_id": "5c076fff35df3a6bd5239bd9",
                "id": "UHJvamVjdDo1YzA3NmZmZjM1ZGYzYTZiZDUyMzliZDk=",
                "name": "IceTetsing",
                "desc": "Project for test ice service",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "innovationservices"
                },
                "updatedAt": "2018-12-06T10:30:06.737Z"
            },
            {
                "_id": "5c1089fe35df3a6bd53653d4",
                "id": "UHJvamVjdDo1YzEwODlmZTM1ZGYzYTZiZDUzNjUzZDQ=",
                "name": "Retail-chatbot",
                "desc": "To create a conversation of a retail customer care",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2018-12-12T04:09:35.221Z"
            },
            {
                "_id": "5c109e0835df3a6bd537104c",
                "id": "UHJvamVjdDo1YzEwOWUwODM1ZGYzYTZiZDUzNzEwNGM=",
                "name": "RetailChatbot",
                "desc": "Project for retail domain",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2018-12-12T05:35:16.366Z"
            },
            {
                "_id": "5c109ff335df3a6bd5372b47",
                "id": "UHJvamVjdDo1YzEwOWZmMzM1ZGYzYTZiZDUzNzJiNDc=",
                "name": "RetailChat",
                "desc": "retail domain ",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "smart"
                },
                "updatedAt": "2018-12-12T05:43:15.860Z"
            },
            {
                "_id": "5bfacb1a35df3a6bd5efc548",
                "id": "UHJvamVjdDo1YmZhY2IxYTM1ZGYzYTZiZDVlZmM1NDg=",
                "name": "excite-chatbot",
                "desc": "enable communication through excite",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2018-12-14T09:58:25.118Z"
            },
            {
                "_id": "5c122a6635df3a6bd5417804",
                "id": "UHJvamVjdDo1YzEyMmE2NjM1ZGYzYTZiZDU0MTc4MDQ=",
                "name": "Fabtemp",
                "desc": "test ",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2018-12-13T09:46:16.003Z"
            },
            {
                "_id": "5c2c941f6594a8026ca84a09",
                "id": "UHJvamVjdDo1YzJjOTQxZjY1OTRhODAyNmNhODRhMDk=",
                "name": "ProductMentions",
                "desc": "To identify product available",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2019-01-03T10:33:22.639Z"
            },
            {
                "_id": "5c35d9b36594a8026cbcb59d",
                "id": "UHJvamVjdDo1YzM1ZDliMzY1OTRhODAyNmNiY2I1OWQ=",
                "name": "HPS",
                "desc": "To design a conversation for doctor-insurance company",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2019-01-09T11:23:31.969Z"
            },
            {
                "_id": "5c3721eb6594a8026cc104df",
                "id": "UHJvamVjdDo1YzM3MjFlYjY1OTRhODAyNmNjMTA0ZGY=",
                "name": "emai-pdf",
                "desc": "pdf doc processing",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "innovationservices"
                },
                "updatedAt": "2019-01-10T10:44:01.109Z"
            },
            {
                "_id": "5ca71e516e08183753dbede7",
                "id": "UHJvamVjdDo1Y2E3MWU1MTZlMDgxODM3NTNkYmVkZTc=",
                "name": "GenomaEnglishProjectsampletest",
                "desc": "english tickets",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "innovationservices"
                },
                "updatedAt": "2019-04-05T09:22:27.280Z"
            },
            {
                "_id": "5cc6f09e6e081837531772d2",
                "id": "UHJvamVjdDo1Y2M2ZjA5ZTZlMDgxODM3NTMxNzcyZDI=",
                "name": "Cigna-CheckBox",
                "desc": "Cigna check box trial",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "smartdemo"
                },
                "updatedAt": "2019-04-29T12:39:59.621Z"
            },
            {
                "_id": "5ccaacb56e081837532661c0",
                "id": "UHJvamVjdDo1Y2NhYWNiNTZlMDgxODM3NTMyNjYxYzA=",
                "name": "Cigna-ListCheck",
                "desc": "Checking List",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "smartdemo"
                },
                "updatedAt": "2019-05-02T08:39:17.823Z"
            },
            {
                "_id": "5cd1532e6e081837536bb2d2",
                "id": "UHJvamVjdDo1Y2QxNTMyZTZlMDgxODM3NTM2YmIyZDI=",
                "name": "InfyDemoForTest1",
                "desc": "InfyDemoForTest1",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2019-05-07T09:43:11.555Z"
            },
            {
                "_id": "5cd3eedf6e0818375381d740",
                "id": "UHJvamVjdDo1Y2QzZWVkZjZlMDgxODM3NTM4MWQ3NDA=",
                "name": "UseCaseTestDummy",
                "desc": "UseCaseTest Dummy",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2019-05-09T09:12:00.188Z"
            },
            {
                "_id": "5cd8fe266e081837539656d4",
                "id": "UHJvamVjdDo1Y2Q4ZmUyNjZlMDgxODM3NTM5NjU2ZDQ=",
                "name": "BuyBot",
                "desc": "Bot that buys",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2019-05-13T06:09:54.413Z"
            },
            {
                "_id": "5a057b42c8435ee1bc9f7cc1",
                "id": "UHJvamVjdDo1YTA1N2I0MmM4NDM1ZWUxYmM5ZjdjYzE=",
                "name": "travelservice",
                "desc": "travelservice",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Nov-10-2017 10:16:28."
                },
                "ir": {
                    "status": "training_failed",
                    "status_message": "Add more intents for intent training"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2017-11-13T07:51:54.108Z"
            },
            {
                "_id": "5a6eb75227aacd44abca5e9e",
                "id": "UHJvamVjdDo1YTZlYjc1MjI3YWFjZDQ0YWJjYTVlOWU=",
                "name": "myConfidenceBuilder",
                "desc": "GreetingCompliments",
                "ner": {
                    "status": "trained",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "training_failed",
                    "status_message": "Add more intents for intent training"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "dineshjallu"
                },
                "updatedAt": "2018-01-29T05:55:44.909Z"
            },
            {
                "_id": "5a815d7c27aacd44abf2726e",
                "id": "UHJvamVjdDo1YTgxNWQ3YzI3YWFjZDQ0YWJmMjcyNmU=",
                "name": "botsample101",
                "desc": "chatbot for a coffeeshop",
                "ner": {
                    "status": "trained",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "training_failed",
                    "status_message": "Add more intents for intent training"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-02-12T09:25:41.668Z"
            },
            {
                "_id": "5a81982627aacd44abf4fac3",
                "id": "UHJvamVjdDo1YTgxOTgyNjI3YWFjZDQ0YWJmNGZhYzM=",
                "name": "DhanChat",
                "desc": "Testing",
                "ner": {
                    "status": "trained",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "training_failed",
                    "status_message": "Add more intents for intent training"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "infinitylabs"
                },
                "updatedAt": "2018-02-12T13:35:45.668Z"
            },
            {
                "_id": "5a8b905127aacd44ab123dbc",
                "id": "UHJvamVjdDo1YThiOTA1MTI3YWFjZDQ0YWIxMjNkYmM=",
                "name": "Travel-PlannerApp",
                "desc": "Travel-PlannerApp",
                "ner": {
                    "status": "trained",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "training_failed",
                    "status_message": "Add more intents for intent training"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "xduser"
                },
                "updatedAt": "2018-03-07T18:45:21.951Z"
            },
            {
                "_id": "5b1df856e918780a05a9c0a9",
                "id": "UHJvamVjdDo1YjFkZjg1NmU5MTg3ODBhMDVhOWMwYTk=",
                "name": "priceChatBot",
                "desc": "Chat bot used to indicate the price  of the product",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity recognition model published successfully on Jun-11-2018 05:24:11."
                },
                "ir": {
                    "status": "training_failed",
                    "status_message": "Add more intents for intent training"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "walmart"
                },
                "updatedAt": "2018-06-11T04:23:12.455Z"
            },
            {
                "_id": "5cf502c2308aae6a117c0243",
                "id": "UHJvamVjdDo1Y2Y1MDJjMjMwOGFhZTZhMTE3YzAyNDM=",
                "name": "CareMoreCheckin-V5",
                "desc": "CareMoreCheckin-V3",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "smart"
                },
                "updatedAt": "2019-06-03T11:21:39.598Z"
            },
            {
                "_id": "5d033bb8308aae6a11983d87",
                "id": "UHJvamVjdDo1ZDAzM2JiODMwOGFhZTZhMTE5ODNkODc=",
                "name": "Project-NER-01",
                "desc": "Testing Project - Remya",
                "ner": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "ir": {
                    "status": "new",
                    "status_message": "Some checks haven't completed yet"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "visualice"
                },
                "updatedAt": "2019-06-14T06:16:26.794Z"
            },
            {
                "_id": "5d1307e1144b3514032447e6",
                "id": "UHJvamVjdDo1ZDEzMDdlMTE0NGIzNTE0MDMyNDQ3ZTY=",
                "name": "WalmartPOC",
                "desc": "To categorize user queries",
                "ner": {
                    "status": "trained",
                    "status_message": "Entity training completed successfully."
                },
                "ir": {
                    "status": "trained",
                    "status_message": "The Intent model has been successfully trained"
                },
                "visibility": "public",
                "createdBy": {
                    "username": "smartdemo"
                },
                "updatedAt": "2019-06-26T05:51:32.879Z"
            }
        ]
    }
}

#######################################################################################################################
Fetch Projects by Name:

Query:
const FetchProjectsByNameQuery = `
query FetchProjects ($name:String!) {
    projects(name: $name) {
      name
  }
 }

`;

Request URL:
http://ice-xd.southindia.cloudapp.azure.com:3001/project/manage

POST Data:
{"name":"ddd"}

JSON Response:
{"data":{"projects":[]}}

#######################################################################################################################
Save to Datasource:

Query:
const saveDatasourceQuery = `
  mutation AddDatasource($input: addDatasourceInput!){
    addDatasource(input: $input) {
      changedDatasourceEdge{
        node{
          serviceid
          id
          _id
          utterances{
            utterance
            case_converted_utterance
            ir_trained
            ner_trained
            mapping
          }
          entities
          intents{
            name
            description
            createdAt
            modifiedAt
          }
          trainEntity
          trainIntent
          predefined_entities
          patterns{
            pattern
            entity
          }
          phrases{
            phrase
            entity
          }
          synonyms{
            synonym
            word
          }
        }
      }
    }
  }
`;

Request URL:
http://ice-xd.southindia.cloudapp.azure.com:3001/project/manage

POST Data:
{
    "input": {
        "clientMutationId": "random",
        "utterances": [],
        "entities": [],
        "intents": [
            {
                "name": "No intent",
                "description": "Add the utterances that should not be labelled as any of your intents here."
            }
        ],
        "patterns": [],
        "phrases": [],
        "synonyms": []
    }
}

JSON Response:
{
    "data": {
        "addDatasource": {
            "changedDatasourceEdge": {
                "node": {
                    "serviceid": "0ApEMWqNhxOL1LbuDWXXH21rNSdqPiPp10EetFnmUCBdHYzmontcs8ZIdFzyofuq",
                    "id": "RGF0YXNvdXJjZTo1ZDE0NzY5ODE0NGIzNTE0MDMzMDcxZmE=",
                    "_id": "5d147698144b3514033071fa",
                    "utterances": [],
                    "entities": [],
                    "intents": [
                        {
                            "name": "No intent",
                            "description": "Add the utterances that should not be labelled as any of your intents here.",
                            "createdAt": "2019-06-27T07:56:08.448Z",
                            "modifiedAt": "2019-06-27T07:56:08.448Z"
                        }
                    ],
                    "trainEntity": true,
                    "trainIntent": true,
                    "predefined_entities": [],
                    "patterns": [],
                    "phrases": [],
                    "synonyms": []
                }
            }
        }
    }
}

#######################################################################################################################
Get Project status:

Query:
const getProjectStatusQuery = ` query GetProject($id:ID!){
  project(id: $id){
    ner{
      status,
      status_message
    }
    ir{
      status,
      status_message
    }
}
}  `;

Request URL:
http://ice-xd.southindia.cloudapp.azure.com:3001/project/configure/5d147697144b3514033071f8
5d147697144b3514033071f8 is the project id.

POST Data:
{"id":"5d147697144b3514033071f8"}

JSON Response:
{
    "data": {
        "project": {
            "ner": {
                "status": "new",
                "status_message": "Some checks haven't completed yet"
            },
            "ir": {
                "status": "new",
                "status_message": "Some checks haven't completed yet"
            }
        }
    }
}

#######################################################################################################################
Fetch projects to import:

Query:
const FetchProjectstoImportQuery = `
query FetchProjectQuery($createdBy: ID!){
      UserTrainedProjects: getProjects(createdBy: $createdBy, status:"trained", visibility:"private", masterBot: false){
     ...projectFields
      },
      PublicTrainedProjects: getProjects(visibility:"public", status:"trained", masterBot: false) {
     ...projectFields
      },
    }

    fragment projectFields on Project {
      name
      _id
      serviceid
    }

`;

Request URL:
http://ice-xd.southindia.cloudapp.azure.com:3001/project/manage

POST Data:
{"createdBy":"58b79a695c280914dc30554b"}
58b79a695c280914dc30554b is the user id.

JSON Response:
{
    "data": {
        "UserTrainedProjects": [
            {
                "name": "masterbotdemo",
                "_id": "5cf645ed308aae6a118094eb",
                "serviceid": "0An4SmVBif6EUfxIoDQDsHpJ9FESR5ws8Uwa5aU0NV6JmES1EXtRqxeHaj8aoOrS"
            },
            {
                "name": "testprod",
                "_id": "5c6f91c46e081837537e687d",
                "serviceid": "0AdR1cjc32ojLZWZV0NwBfiHjjS2Oo321QfCrC987z2Cn3bZW1PttymdW1H7bCrN"
            },
            {
                "name": "testprod2",
                "_id": "5c6f941e6e081837537e8123",
                "serviceid": "0AdR4BQ7WvjhBLH0bgtAfia8BLwUzXZD8qmvYyIGJ3n20B3s15A5ml3ZLI9dryUD"
            },
            {
                "name": "testprod3",
                "_id": "5c6f9dfb6e081837537ee544",
                "serviceid": "0AdREkEwYbPydZg77pBBBs8c4ML10ZuqlPys3Cdm2lEYPBSB9M8tHCvcb9bcvF2b"
            },
            {
                "name": "slavebot1",
                "_id": "5c6fb0a96e081837537feca5",
                "serviceid": "0AdRYopQfMeIrP7hSM5LxfpxAz3hzjTcfI9ZIx1G2VboIC4URkAdMD6Kbu7phRuX"
            },
            {
                "name": "masterbottest",
                "_id": "5c6fb13c6e081837538001e9",
                "serviceid": "0AdRZQYuIVatdEE1g0615YXgiCSPVevOwpgFWYEdS3gcDb1H7wbRpvXYVsk8uRMU"
            },
            {
                "name": "testNER",
                "_id": "5cef9c46308aae6a11715f92",
                "serviceid": "0Amauf6U4W714xX1BbhV08g0Ki7WzR2hznHhyKMqvjmYcbHKUMSqvPF3qpol7FVW"
            },
            {
                "name": "testspanishdemo",
                "_id": "5cf89f5d308aae6a11815960",
                "serviceid": "0AnEsokqlmvAPtkFjV7c1t1SohWwsVS8gJ8Z0YjUDsYknUYTmiPaBBtAL25AMdyy"
            },
            {
                "name": "TestDelete2",
                "_id": "5d120b26308aae6a11b91b6d",
                "serviceid": "0Ap3d9QvxJkLjd0uPjYq5iDAVScfElZRYxq8D0JdyE5rlxUUUFz6b6nzx94U2D1E"
            },
            {
                "name": "TicketIntent",
                "_id": "5d1332bc144b35140326d649",
                "serviceid": "0Ap8keicJzofV3KWWwObaFLUdnRARG7KG185ZQFPcXn5Up3zQr8ikTLPycm5zDQe"
            },
            {
                "name": "MasterBOT-DesignerTest",
                "_id": "5cf9eff6308aae6a1183b138",
                "serviceid": "0AnKiNbM7RazgjPHpPmYrtWQblDDjwrfByiuNzBaJJa3zJYxWEmEnYEkQEwk9HnK"
            },
            {
                "name": "E2ESample",
                "_id": "5cfe01ab308aae6a118a8aca",
                "serviceid": "0AnclKP6jDgbdYUyNnSvkRRyVssRqeDTlh2tog4tTmGg6XhCrtFVu9G34xQhXuxI"
            },
            {
                "name": "New-booking-Assistant",
                "_id": "5b0544c50e8e769cc4409c29",
                "serviceid": "0ADW9IldZrdTjIIscoC3Lyta5ioCPEiDjsEePIi5kJIFFynW235RJde7MvWLAksn"
            },
            {
                "name": "demo-project",
                "_id": "5b4c6956c9a9b809e138e0b7",
                "serviceid": "0AIbgbzcu9j9F5S5gBE99WkBh4aVV3jB7mzW38ox6C9Q6aDOZ93Yip0McfoGDCsw"
            },
            {
                "name": "TestBot",
                "_id": "5b92481f359c7f2417edd6c5",
                "serviceid": "0ANbZUUKmS89JenyugWktSw1NUS1iErRo023qrkrcXDOXO4Rl0IiSEnuBGzQw4JA"
            },
            {
                "name": "Testbooking",
                "_id": "5b98b631ee011d7ae1aac820",
                "serviceid": "0AO45b6Y0K4nktUJVeXfHSJPxJQqsp97IER3GjcqF1LVG2F2lof7jBsvtj2Ps3Zs"
            },
            {
                "name": "MasterDemo",
                "_id": "5badfd7cfc5bf109622d96ea",
                "serviceid": "0APaSmtazyfjRbnrsYRXVKux8Y6zEmfKuDf8Dprgme2Y9CLuBK9n1VrHUNFy7yge"
            },
            {
                "name": "testt-hello",
                "_id": "5b3f1163c34a360b9dab0541",
                "serviceid": "0AHeV638ufgWSGJhuMCnf8c40nA1MjSgizzkhKvm3hq4mw9WCcYFFK1hoKze6GoQ"
            },
            {
                "name": "TestAisleLocator",
                "_id": "5bf52edf35df3a6bd5e348d6",
                "serviceid": "0AUgDYdIUYNJ3o5yCeKnbnkdr6jc2mk9mJWVPxFosPZJuH5vgaIuB6m4S9xCbQjT"
            },
            {
                "name": "TestEntity",
                "_id": "5bf533d735df3a6bd5e3bfa2",
                "serviceid": "0AUgIsoyZEsD9pKs1jcH3AFUOpX8peA95FsJUWEO4HBbUICrBSvJKjHWCOWY6mtI"
            },
            {
                "name": "Intent-Issue-test",
                "_id": "5bf5344835df3a6bd5e3c699",
                "serviceid": "0AUgJMBtVXDaj23HpUGJu2Yc7NujpUzX5OFmF0gcRmJhdoIueLgY5DFfPuUPEaMC"
            },
            {
                "name": "MedicalAssistant-NovTest",
                "_id": "5bf7a71935df3a6bd5ebdb54",
                "serviceid": "0AUrAeezHZDUOYFdPifncoInagDBtMuSXQHRzHAvLyK5uhM91GLTRwOggCtoAjUh"
            },
            {
                "name": "test-ascii",
                "_id": "5c0e0ef735df3a6bd52cda95",
                "serviceid": "0AWSXq2niNbu9umohERbNQqA5gv7KXrOkWmeG6AoTennXcIJwUe5KcQgP4BvTPBI"
            },
            {
                "name": "MedicalAssistant",
                "_id": "5afaa28a0e8e769cc429817e",
                "serviceid": "0ACkzFMgp25BEJweE5DAFJ9L0RylN7pblzZNWElZdIlvOuZlPsmqsOtl9q3N8Day"
            },
            {
                "name": "xzxcsdv",
                "_id": "5c2c687a6594a8026ca6affb",
                "serviceid": "0AYd9SF2lkbgwsQGHePSf2MFjlCCSdo1c62Hxx1mHMWEX3oE1SvqHBA0q47EtaHC"
            },
            {
                "name": "regex-adding",
                "_id": "5c08beb635df3a6bd5264e12",
                "serviceid": "0AW4yiXncMmFLcenY9iU05tVIg7skdLN6cMXishMWfChqIGwLlCtFFCxknUagS52"
            },
            {
                "name": "bugFix",
                "_id": "5c501122d93bb76649cca4df",
                "serviceid": "0AbBJ03AeVUH7uQs0Xn0jSumntsNh5OkBw0ixmYafL6aasGqcqYc795eWNRwdGNs"
            },
            {
                "name": "PasswordResetProject",
                "_id": "5cb5bb566e08183753f72c58",
                "serviceid": "0AiSD2ffnNHTQ3wJho7WmMZKxhQVlQ4OhrIECTe4cj1CiJkwVjoG5QLcgcoHZeks"
            },
            {
                "name": "test-ss",
                "_id": "5cd14c5f6e081837536ae2a2",
                "serviceid": "0AkQTMO0QVF0zSDtgf0vCgbG7pFZvHWxyhaSUctTqhKZPDRDe2NLq7uOQOR1ZTis"
            },
            {
                "name": "UITest",
                "_id": "5bd19ab4a973d070442356e2",
                "serviceid": "0AS8Q0Zd9ptR0ee4wj1qxZe4o4TtMf5wLKkeUxv3AEcvOXKWlFjzxpAySxboO9Wn"
            },
            {
                "name": "demo-ss",
                "_id": "5cd2d5b36e08183753795e67",
                "serviceid": "0AkXHqqR4LXd8m4gkObRq73HFv3CeGqOAHwic2wHTx8swOAYd9xKFAYukhXzC3cE"
            },
            {
                "name": "testttttsynonym",
                "_id": "5ce522646e08183753dc4349",
                "serviceid": "0AlqRufANIcpGxQLt0Pc73Sxqr7Qlm03uo2fZ9eAgdY2qhA4WSgeS1AVtNi2W5Sv"
            },
            {
                "name": "testsynonymmay23",
                "_id": "5ce68cfccc2de34bff30d37d",
                "serviceid": "0AlwjOPyCCLll4ghW9eJVg7AKIfy4wsgsWuNgTc1jWNG2SuJKyQrQefTGoU0tvrB"
            },
            {
                "name": "testspanish",
                "_id": "5ce7c12747cf4e7274613839",
                "serviceid": "0Am24Pju5LvDIuLB9vJIVoPgGeu5xtqzoDcJIsdG7gmVDeFFEQ5qyInHa6bTOXWr"
            },
            {
                "name": "test-clones-demo",
                "_id": "5ceb8deb47cf4e727461fc1d",
                "serviceid": "0AmIvJMRumk3g9FpADxgV3uqHbnWd3FBbKjNzYSEdmWs1rfXtV4bgvbuOKbsTo0g"
            },
            {
                "name": "testimport2",
                "_id": "5b98dec8ee011d7ae1abd144",
                "serviceid": "0AO4n96i6WlEurYjQUssjl9Ob9w5Xd2ibLx277yDNnbrZ6XZv5F9U9b3qr8wdmDU"
            },
            {
                "name": "MedicalAssistant-Spanish",
                "_id": "5bd2ebbfa973d070442acc77",
                "serviceid": "0ASEG2xEkcTEoUEcm4oAYxEcxXMVoikDtzsWg8Om8KPubambVC68Hb5us45rwBsw"
            },
            {
                "name": "test011",
                "_id": "5ce6401dcc2de34bff2cd14f",
                "serviceid": "0AlvOpUReZCJ6UgHyUN0NqTPGixV8vyfI1qfBO2LJtXr4dpNIECkKSfKSWkZdIZp"
            },
            {
                "name": "testbot",
                "_id": "5cf0c8c2308aae6a1174c4e1",
                "serviceid": "0Amg7Q9XVl7fcZU5RyzhjbhyosDCr5Qvg5bnqz5ZeoUL9hxxhVQi9kbLxZLDdLnQ"
            },
            {
                "name": "testchildbot",
                "_id": "5cf649ce308aae6a11809e31",
                "serviceid": "0An4WwwkcU8VgcTUpJVxj2inZWcgizxSp8SPJZ5vlys2rpfhqkC7CxCjH1I9WVAM"
            },
            {
                "name": "BOT-DesignerTest",
                "_id": "5cf8b0f6308aae6a11816bf0",
                "serviceid": "0AnFBifULzGOs1vgzp4kjTKQ4EFMFVNziJfWKaypCty6RieIKm21bESvdgTjZCHD"
            },
            {
                "name": "bookingticket",
                "_id": "5cfe40a4308aae6a118c0ffd",
                "serviceid": "0Andqy03muBiKiLjFF9qHqW2cg7PZ0nV4bADrhHCShnQjobOc9VK7FKyF9s2CdxD"
            }
        ],
        "PublicTrainedProjects": [
            {
                "name": "ATM-PIN-Reset",
                "_id": "5952a1a1c9c57fd148d088eb",
                "serviceid": "09iQSyU0GQ1qzKq7HJ8a89Bs52nYmD36JcuTyl373O7fbgmYov6NmXqmN8RiL2yJ"
            },
            {
                "name": "satsuma",
                "_id": "59631e51c9c57fd148d089f0",
                "serviceid": "09jbh5TXkHhHTepzrWbQqKzoy5Alr45ZwXQ38V0ivCBvqL2mUDRNWXkLohXnalt0"
            },
            {
                "name": "example1",
                "_id": "5965a976c9c57fd148d08b8f",
                "serviceid": "09jmqzfmvkU9CmOxR40E40YTp3FGvO5WhQSsZUX9iFJTOXE43AuPlpV81hPHFVz9"
            },
            {
                "name": "intent-test",
                "_id": "5965bcb2c9c57fd148d08c4a",
                "serviceid": "09jnCMpx2xQEFeVB3HEn8hUnJKMTEvmNymp8x66ji5CO86QrgvCIwWZRo9nGY1gY"
            },
            {
                "name": "resetpassword",
                "_id": "59783cc2fc97be6468dbf981",
                "serviceid": "09l7EyHBMMh3Cy1oU2Q70zasgyTEh7HIT4YhRtI41ykAxXVnKZxiVz62J62swTuX"
            },
            {
                "name": "clonesResetpassword",
                "_id": "597853bbfc97be6468dbfad1",
                "serviceid": "09lEHIAl8qQBgwrafmcJHmv52ha6YUw7e0tfd9uqA2qEHgNXZXevypxmHNDFAMRy"
            },
            {
                "name": "Email",
                "_id": "5979a4d7fc97be6468dbfd1c",
                "serviceid": "09lDfVcdeWRNSUZhJwBPNCZ0s3yHZqMhoqcsJ5YPr6sK0wHbD6nhTfcxvrvkCv2w"
            },
            {
                "name": "PASSWORD",
                "_id": "5979c24efc97be6468dbfdf8",
                "serviceid": "09lE0R2NRDyj9fl9pGkncp2axZuo1NJ1y0tqj9jqeV1JACSgwXkLQjwKbbaN6LEK"
            },
            {
                "name": "WoltersKluwerService",
                "_id": "59899c752dddf78c7352e99e",
                "serviceid": "09mMJfNM9HTLZxOa0Pkl5s8RQH4M6iU7uBxbk6dRI39AdGG1JJYh8NdCwBIphZIU"
            },
            {
                "name": "UMA",
                "_id": "598af8c92dddf78c7352edbe",
                "serviceid": "09mSbFbKGWEnPreXyF5dnFTWmXHvOSyCOoeJu9yLuGzFgpGJgqSj0L20AaN6HCcG"
            },
            {
                "name": "WolterKluwerPOC",
                "_id": "5993ed762dddf78c7352ef20",
                "serviceid": "09n63MI8wyGYwqJ54Y9UA8Suzk6A4UOxhRvtpDBpEXHYbRRVHCF6JwGzERPOyrH5"
            },
            {
                "name": "TravelRequest",
                "_id": "59a7e8de4336f9ff03d22100",
                "serviceid": "09oWh7OlYRId7n78glxcWiI2H5O3b2486UCS2jYOttj5ValoXaz4ns0a7KVgijQa"
            },
            {
                "name": "HealthCare",
                "_id": "59bb6420bf2a64c5c0bb3a9e",
                "serviceid": "09pv5OqWlxG2hvyJny5ba6d5X3PsZgTEE4cMJGXW3beNhDWVOiK5UGoCoh1JfZJO"
            },
            {
                "name": "JaideepTest",
                "_id": "59ca0a3fbf2a64c5c0be1c98",
                "serviceid": "09qy357pkkskEdiT8wtA97rAZxnCY32eulJNhL7LozSbjVmtww0FFfZLM2GDPtUd"
            },
            {
                "name": "JAYANTEST",
                "_id": "59cddbd46c75b1e7dec8f014",
                "serviceid": "09rEz7ECxdYyd7BjdZMMdwqXduYVqzyD6OMtEsihTWWrx2SuGIjHyIbIIyozSN1X"
            },
            {
                "name": "DEMO",
                "_id": "59d467c56c75b1e7dec94789",
                "serviceid": "09ri1JHefWG1aW0LpumBUhzrpjKSOEvvSSwagx7vmrQDBFPR8ySAcxavDvm2zC9s"
            },
            {
                "name": "deepthi",
                "_id": "59df0d47df0d8943fc68f08f",
                "serviceid": "09sTEwcL1QsdUiDIYWWFhM4uA1RXSdgOYB1j0IwU2HGgcOezfHnq6VoNYnCQu75T"
            },
            {
                "name": "conversation-engine",
                "_id": "59e05e64df0d8943fc68fbc6",
                "serviceid": "09sZ59nWuSFtTGWKR5SufAxVliaF8UhIb3O4k4vp0LUJJMZTk4nHy2G9yoYgmMLx"
            },
            {
                "name": "ramtest",
                "_id": "59e5d8a7df0d8943fc694856",
                "serviceid": "09sxNGcZK7oG1SRDyW2zssABygocjJlNmwSdMqCTlk0sZoLSl65shgjBDH645IKa"
            },
            {
                "name": "ChatBotDemo",
                "_id": "5ab61411c9b8e8bacbcee0d7",
                "serviceid": "0A7qvcOUJaeTqBdc5Lj2d3pGQNF2FtDvq5qsnYPtLm34Tis2O5SfRPJ5XnXd8OKA"
            },
            {
                "name": "InnovationLabTestProject",
                "_id": "5ab8d964c9b8e8bacbd2bc7d",
                "serviceid": "0A83DNX3KiPngVOYRWcGlGmey4v0jBvrgf3cLYdimInuTFTy7yK3J5YoxeJ7l9rB"
            },
            {
                "name": "MipaNLP",
                "_id": "5bcf0faae366630b19bdb8c0",
                "serviceid": "0ARx8rYTpTURW59sUqKb6OmyUZIfuKL0eDQvE2U7RND1TBdsUulS7ovorlp8C7Mv"
            },
            {
                "name": "BootsPOC",
                "_id": "5a01c5bdc8435ee1bc98bce2",
                "serviceid": "09vV1s9TY3o05ZA8FqUCqpW89ka8jKssLA8ISwf4KFM7kkwHGGBCjGwsgPFwwXvO"
            },
            {
                "name": "wish",
                "_id": "5a052feec8435ee1bc9bfd5f",
                "serviceid": "09vCNZYR1XwU9tDgXBqAQjuhBkZKYj4xi3Y6wKBB92IWaFVjqv7y2N6qOMsHMKzl"
            },
            {
                "name": "Travels",
                "_id": "5a096c5c8063312a5c66b7d5",
                "serviceid": "09vVASwcb5QtM1hVSk3n82MuBVquhUUBrW4SgLKiZV0n35SFdisjr7YvML9BvPAJ"
            },
            {
                "name": "serveraccess",
                "_id": "5a129e3131121f93b722d1d6",
                "serviceid": "09w9wgW3FejhngPsxSt7EicFrU6A2MLGVKfAeIb7hz0mphMZ1ImYFoQ9jwsAzphb"
            },
            {
                "name": "travelbotsample",
                "_id": "5c6fb90f6e0818375380e0dc",
                "serviceid": "0AdRhpcCwi2JmQgdagFK8YJluevkCgs85voHITAI4fBo6aS2zMJNh87N4xFfqBi6"
            },
            {
                "name": "Test123",
                "_id": "59e5822adf0d8943fc692bd4",
                "serviceid": "09svscW1bvVEx6AvJFL0ByI1xX6ExVv0WDmtV05auWzK0uwrYlnDCOfSbZC3ggyz"
            },
            {
                "name": "Boots",
                "_id": "59e85bb5df0d8943fc69b524",
                "serviceid": "09t8WrwyGohkevaeh5ZWz0SMMo7oBocRM51Wb9mGQKefH8GqX0BqVU1QVYy3Y19v"
            },
            {
                "name": "Test-SreekanthC",
                "_id": "59e991e7df0d8943fc6a1758",
                "serviceid": "09tE9Uon0qLcJlz1fgx3D8VBxBALfR1f4kry8ylhu4eP6EPAEAEtJRPEqpNAq2mV"
            },
            {
                "name": "chatbot",
                "_id": "59edd24fdf0d8943fc6ad613",
                "serviceid": "09tWl3ZcTipQzL8QXX08l7CWOdqO5QKVlFUX492Lw6PlQiDcjnFt2r9AOMRnS4TV"
            },
            {
                "name": "helloworld",
                "_id": "59f0789ddf0d8943fc6b25f2",
                "serviceid": "09tiUtULCLmEk8cG5GcPrdqtOES74JJ1R0PnmM5J6QwJJjPl6Bv7j7ZS562dISSZ"
            },
            {
                "name": "MyDoc",
                "_id": "59f2bae4df0d8943fc6b7a8f",
                "serviceid": "09tsWAUkp9HvdkSO05NvdNRWFw1kXGimwhwM5vxcatKZ2zudLJt2v4uAj42bWcAo"
            },
            {
                "name": "SAMPLETEST",
                "_id": "59f30567df0d8943fc6b9ca9",
                "serviceid": "09ttoBwqCGmD4BZO51wABFMU80jOmSUiZQRRkMDX8vMd3GIbXai3ycHizGDX0fNR"
            },
            {
                "name": "cloneshelloworld",
                "_id": "59f6ec28df0d8943fc6c1785",
                "serviceid": "09uB6yxqko6lU9FtgDGuQcMUtOAcZe5sPhQ6b4Y5U0pMbrH1Ai9ghS1sbx7jc4Fi"
            },
            {
                "name": "Mydeen123",
                "_id": "59f8622edf0d8943fc6ca485",
                "serviceid": "09uHalmlUEHtypCBrLLvjRUnI34JdmfvVImTiVrhDWw2uT3g9OJV14xqlp2Hlp5I"
            },
            {
                "name": "DemoTraining",
                "_id": "59f99ff5df0d8943fc6d1ff7",
                "serviceid": "09uN62v8amSt35qhbBhuje1nPRe4AXRL9VkqGGwip1GetcfxnwzzLGHynWFvWwpq"
            },
            {
                "name": "bootsResetPassword",
                "_id": "59fd604b3bbf886d100ef485",
                "serviceid": "09udjjxyNFZNNeHbc4zuI45M8gC6gVTGsE5aOQuGrE4HIIGWsc4itwdAxlSiE7Ad"
            },
            {
                "name": "sapsrmbootspasswordreset",
                "_id": "59fe1c673bbf886d101017ae",
                "serviceid": "09uhMqN6fpCzexaqdlzgWW3LrC0UTrzNNBrHWmrcZ7y2siQhXz67sO4B7uti5DJf"
            },
            {
                "name": "demo2",
                "_id": "5a00061a745faecb410f39c2",
                "serviceid": "09upTepM0GgmkeeLSe3RB7NVg6b9lCrBKsmLtocMto4AXGyXrL9arsmRu2PKr5FP"
            },
            {
                "name": "QAAdvisor",
                "_id": "5a053e76c8435ee1bc9d12a9",
                "serviceid": "09vft9Mh0NRD4P4j8GEH7LIEkkl7ex7S0MdLcAFijv9OEZZI66Yl81Y1gbk7TPYh"
            },
            {
                "name": "College",
                "_id": "5a057027c8435ee1bc9e8f86",
                "serviceid": "09vDUas2h1QWopCCqeokwNUhBeidfbEP3MeLkpJFMwSiiRXXjIxsvAAkRwA7QCjf"
            },
            {
                "name": "test-nicy",
                "_id": "5a057241c8435ee1bc9ecaa8",
                "serviceid": "09vDWmVq9X9Jtogupa6h9A3lyxRb9oVazvwbNZ5TAAx1LuX9LJE0YlWa5n0uPocc"
            },
            {
                "name": "BootsChat",
                "_id": "5a05767ac8435ee1bc9f4e1c",
                "serviceid": "09vUOFOAv9D7fA1ZkaO8dsZr1gYXNt2fObIq9P4IGFSCrhOZHmhFCZ4tpQ2wpjNB"
            },
            {
                "name": "test-nc",
                "_id": "5a058cd2c8435ee1bc9fbe7f",
                "serviceid": "09wpEVKS3tMZwiYoTSh6oZQMxn4nsAPxnBLvY35xLJ6eT7G0ZI9CeOvUwrdtKWaa"
            },
            {
                "name": "AutOpsLearning",
                "_id": "5a0947208063312a5c637a7b",
                "serviceid": "09vUWJVtz22EXsk95quBnZaScjyVjK7AcO0dkb978mEOxTAxjKhO6YVJyWKMxaDG"
            },
            {
                "name": "testTraining",
                "_id": "5a0954cf8063312a5c65cd10",
                "serviceid": "09vUlCCOC2vge9G2rRd59SRGmP1r1BCYfVhpfFiqQ9OBvjVqasXmdpzewawaGdrr"
            },
            {
                "name": "appledemo",
                "_id": "5a095f588063312a5c66947c",
                "serviceid": "09vUwKCv1xvSSJBjfm9kVN0JDhheC1BWxg26GmpSFrIoihR3B8i8rIepYicvZyG2"
            },
            {
                "name": "PacificDental-Learning",
                "_id": "5a0ea363637019237e71e7ee",
                "serviceid": "09vsLhTSo0grgmnNbGsyx1SaBTjj3b9BPDiyf4vBpyzpk7stXZyaMtwvXTZPIted"
            },
            {
                "name": "Anthem-BPO-RFC",
                "_id": "5a13c85531121f93b723c865",
                "serviceid": "09wF9Y2YEtiJ32lNR1sPbh5f7ChE2TFoFVdOmZFBuc4L3VOLtEbTLRAxkhb0m7HB"
            },
            {
                "name": "AnthemBPO-PasswordReset",
                "_id": "5a15471631121f93b726809a",
                "serviceid": "09wLk5sr88pDGqMYimf6dI3VeHS0LTMtJCL8ULzNnE8N03V00ttdTRKFjbXpsDsz"
            },
            {
                "name": "woltersk",
                "_id": "5a278a86fba8195fe9580d29",
                "serviceid": "09xekLikG1XiLVd5ysox7GNYb0XToAGSmdT8kODIlIyOQSn2XpOeCi5Vbl0QZF8N"
            },
            {
                "name": "Example",
                "_id": "5a27b77ffba8195fe958315e",
                "serviceid": "09xfWXCViKgFRiXW7rqZsg5b2weP4MIXn9QFN2TYvore2SVksia03BzKT0GAeyKE"
            },
            {
                "name": "state-street-test",
                "_id": "5a311485fba8195fe9600187",
                "serviceid": "09yL3Ja1eIVKLKAWK1Ur8UJ7AoCwISYpZfffaPXhsuliGiAPwbGfKS00XIw6FCeR"
            },
            {
                "name": "Testing-Sreejesh",
                "_id": "5a3b40b54e0d078010489222",
                "serviceid": "09z4AVneWNgda1J7e7dL87Ifqq5Ljum05V76nb8xHroN12pj0g3aiVWRzf0ASLXM"
            },
            {
                "name": "Greetings",
                "_id": "5a3b410a4e0d078010489589",
                "serviceid": "09z4CNfHJ8n4Hq4yfwKlX3qocXGFmCpU36FBTx7YSdXlJxEN9PNjnsUnR12l51te"
            },
            {
                "name": "JiraTicketCreation",
                "_id": "5a3b48e54e0d07801048b103",
                "serviceid": "09z4JMlF2VqRfU3nk8TmdHQQDsCGBPIpssx1IZCXYIjtsvr9FQqpD81j4wjHcg5C"
            },
            {
                "name": "Jiratest",
                "_id": "5a3b50ad4e0d07801048b67e",
                "serviceid": "09z4RgzyOjlqBYw0GKx9lVyVpSyUDO3DzbggxQXPYuexj9WOlZuZ2V4zASi6Y9W3"
            },
            {
                "name": "WaltersKluwer-Corpus",
                "_id": "5a3be10a4e0d0780104bd7b9",
                "serviceid": "09z6wmHG32cjOClrRyJyXtXUMt76pIsidYbte1ORqkhLppeIbxmApX2QOpNKJGdH"
            },
            {
                "name": "dummy",
                "_id": "5a3ccec44e0d07801051d5a7",
                "serviceid": "09zB48Vu3faucliDJEDyvQkXzLxc7b95yu74MLElzLDjPsP84osDsJTWbBKVCzb5"
            },
            {
                "name": "WK-EntityExtraction",
                "_id": "5a3e252c4e0d07801052d1a7",
                "serviceid": "09zGzsulQON9dfsI9K5v15fDuPHp13E99wd9uoULExh7rn6p6qOXBPzeYekYb159"
            },
            {
                "name": "ProductIdentification",
                "_id": "5a44a9774e0d0780105b1214",
                "serviceid": "09zjtxdsr3zUP1M0twSSCw2YhVd3wioCZi49v8EhQd8GRkbCN4X3gSIrZ9hdrq20"
            },
            {
                "name": "boots-skypechat",
                "_id": "5a45d6c84e0d0780105d0d19",
                "serviceid": "09zp7hvtuhkOfVsqjuWgWl1FbValAnJguE2ZXrdDa1qvBmFcs0YhPwKP1qXZAHYl"
            },
            {
                "name": "bootssapbusinessobjs",
                "_id": "5a531e5a4e0d078010636ffb",
                "serviceid": "0A0m1CuzrJLUKyuBmQwP1Q4c8fsUTu9eupXCd2zCHBzMjVHOKtTL2S8IXCY1UqAQ"
            },
            {
                "name": "bootscentredomain",
                "_id": "5a545e7d4e0d07801066a2b0",
                "serviceid": "0A0rZ4MFIdbBsDimUGrU3jNQHw2ynYvzb7DKIZkLvihrdihpXkaGBqTYWaznjQsx"
            },
            {
                "name": "ICEXDTest",
                "_id": "5a5595f04e0d078010693355",
                "serviceid": "0A0wxmk4cHsqJxT9w9KvbdF2G1tGFvQIoqGenVOuJEDzV9tSeJtIItfp4RqTw00m"
            },
            {
                "name": "ICEXDTesting",
                "_id": "5a55a24c4e0d0780106a0acf",
                "serviceid": "0A0xAti1rZzj16IjZn8OutDp663USMjhEa0zMT5MpGPBUwX8BfPtyhJZkpGSTQHH"
            },
            {
                "name": "BootsSalesOrderChatbot",
                "_id": "5a574a0c46b5b87be7ee8ea1",
                "serviceid": "0A14WEwSDWjyKspywdJ95nur0hpoajLITh81G2I7VIcgaAlMMbZkZf6EpMOvmv7P"
            },
            {
                "name": "Healthcare",
                "_id": "5a5e2b9b46b5b87be7f7d4fc",
                "serviceid": "0A1Z31iZvT0LdMCmjZaBcj2Rq503wUmT4tjUmW5JY94TJhxQDNghFn4RuxaYIAOh"
            },
            {
                "name": "Testissue",
                "_id": "5a6079ec27aacd44abbabd31",
                "serviceid": "0A1jGLIeTHh9WKCsMgNMslzkoXBJhKnMrTTsLthBSykBUWRMRgMy83dBiINvRHCQ"
            },
            {
                "name": "CMTest",
                "_id": "5a60a94527aacd44abbad0e2",
                "serviceid": "0A1k5CLYAEnpJgDiQFx7jKSz8p54LuOJk0tZCJj6BcYzUixbEixmDyiwLLS2VJg3"
            },
            {
                "name": "CMTrainTest",
                "_id": "5a633f5427aacd44abbbd9a0",
                "serviceid": "0A1vYLNsxXkhwGV8g98RYIIFVxRP2ytzVJfeFgjg9z86G9cO062bGt4IHAISTZ6l"
            },
            {
                "name": "CMDemotest",
                "_id": "5a65798d27aacd44abbd8de7",
                "serviceid": "0A25QotCyg2Dgwei3Ykfykkjoupp0ZHX0qoPZ4OkgXkrUaPWl4Rdsih8of5aUaia"
            },
            {
                "name": "CMWAImport",
                "_id": "5a6604c727aacd44abc0b4e4",
                "serviceid": "0A27qMvvg2IVSce3JJ3qZH754ONksFkNA076MC3KY1HspkAts45wua7kjkcUO6NK"
            },
            {
                "name": "UPSCompetitorAnalytics",
                "_id": "5a702b7f27aacd44abcea1ce",
                "serviceid": "0A2qroycIdGdcMYLmZi6ZVvVFUGZXXr8JHAA02yswcsvHK8Xs1pdxMah22DFNlYa"
            },
            {
                "name": "Sample1",
                "_id": "5a7150a927aacd44abd0727b",
                "serviceid": "0A2vwipK61McYYKwGo7DGTzI1Q98ED8Zh7yQp0Hkw4p9ZCOXpwFi5rMJ6VjSKItd"
            },
            {
                "name": "Test1",
                "_id": "5a740bad27aacd44abd8ecec",
                "serviceid": "0A383Z6Wcddp0HOKw1yvby0EOzHHq0BfMJaRRymHQuoY1nfmwSYXMNmO9kGiLIy4"
            },
            {
                "name": "Trial1",
                "_id": "5a781cd927aacd44abdb2a6a",
                "serviceid": "0A3Q5wIFGplfnzkqfJvdRGF2nNCv5PxssC54uhHA6VY0LgMmdwszd4lCxX1Hzm7i"
            },
            {
                "name": "robertoTEST",
                "_id": "5a79c90c27aacd44abe08fa9",
                "serviceid": "0A3XVsBlnGfp1phHvg06mbTkXeZn7t1T7vwkwj2oeUySuXLGAx31PMDEqCWLsIVO"
            },
            {
                "name": "TestBOT",
                "_id": "5a7c403927aacd44abe81a25",
                "serviceid": "0A3iRsgMS9z0ljDD9wls9VaQubbVP7TMayPe9KliDYKItcB3ZHUYjL3nnobpdgsL"
            },
            {
                "name": "DocChat",
                "_id": "5a7d3d7a27aacd44abeb4da4",
                "serviceid": "0A3mrsSGZBt0yzpJxJW7gzO6le5cUyff14r2sPUol8pxHFvyG8NVpRJwFeqzGhKT"
            },
            {
                "name": "MedTest",
                "_id": "5a7d476127aacd44abeb7bc0",
                "serviceid": "0A3n0Vxg9nzta3o2tbCZp9NBGzHK5PbTikYMgoR7BJz1WEVHzgONoBkZ6EuemopB"
            },
            {
                "name": "Costco-category-product",
                "_id": "5a7d550627aacd44abeb82b0",
                "serviceid": "0A3nFFg5FnZ8lTT71NScGprJOQbrH4bmckcNTA1eztDmCs7KsbTZgh0hF6aZBs4m"
            },
            {
                "name": "chatshop",
                "_id": "5a817d8027aacd44abf449e0",
                "serviceid": "0A45ggnQjUtyQyFizIlJUHlvpdtxDCKs6sJ0ZTBhaXZ3vP3YoPX94ZoP09Okl5PN"
            },
            {
                "name": "phonedetails",
                "_id": "5a82783127aacd44abf66612",
                "serviceid": "0A4A26dbegMNV9qgANBiZ5XnqYgN82bH9YI3zXkIytBfcBq844MYkvvfwyOf3Cko"
            },
            {
                "name": "Alexa-Demo1",
                "_id": "5a827fff27aacd44abf6eef7",
                "serviceid": "0A4AAkvLqPTaOBJeeW43sm3b9QSgFuBaX4p0hqbpeeqo7rNvUoiosSZ76RjqpmfU"
            },
            {
                "name": "SSTest-AS",
                "_id": "5a8334b427aacd44abfb5e10",
                "serviceid": "0A4DINRGIbJ8fpGnz9mWlKxhNs31DgGCamajY0nWXq6fktIe2mrafmBeYyMWbb3o"
            },
            {
                "name": "MedDeliveryBot",
                "_id": "5a83c15627aacd44abfc8c3d",
                "serviceid": "0A4FjQQ8mRSBJPMNXkWPzPgWjnJ5xcsxt3v60KRe2geEVogjUwnkHQkTXEqaLkTp"
            },
            {
                "name": "DentalAssistant",
                "_id": "5a85006a27aacd44ab002213",
                "serviceid": "0A4LG9w84qRJ9HMjwodpG9t4ZZbUNMPAFeOsoc2WSDUbnEDkL99lA1T1OYgAOviQ"
            },
            {
                "name": "PatientPortal",
                "_id": "5a85025027aacd44ab003740",
                "serviceid": "0A4LLSyGRAs6lKHwc94564cZGA6MOkghYMPVFHkwbEwQTIbKOHIeeOpArjDTuHaW"
            },
            {
                "name": "cab",
                "_id": "5a852d7627aacd44ab009f51",
                "serviceid": "0A4M2dw2H8wZ2eZsQfEtAWbkJyJqFoTwEc38Ctj3rxNGa5qanWUTXjdOcvfQwquH"
            },
            {
                "name": "foodbevarages",
                "_id": "5a86b80e27aacd44ab06c2f9",
                "serviceid": "0A4SsQg93aESoF8Q8nLY4xYZlJzfvcAMMqwb2TeLJ6PxhA3WOUkwUdxv4gezd1b9"
            },
            {
                "name": "Travel-planner",
                "_id": "5a86d04027aacd44ab07258c",
                "serviceid": "0A4TIXNChfulzUkUH7HxlxEfBTXBZrd8DSl5iO3oRVtMot2Q78PaZTGmN4QYeOTx"
            },
            {
                "name": "PizzaBot",
                "_id": "5a892a9327aacd44ab07cf2d",
                "serviceid": "0A4dk82dwODNJ7HKKC9JEGay9sYqOBp0KaYbFhg2uI5Emmyy8KsBhdPOvOqq0ZVd"
            },
            {
                "name": "Aditi1",
                "_id": "5a8a781a27aacd44ab094fd3",
                "serviceid": "0A4jVd4oxBcHXuedwZwTLkjpjSBHXBWBXZta5lIoZfllrYDEEKuLZpF1WyqjDtvC"
            },
            {
                "name": "alexa",
                "_id": "5a8a791627aacd44ab09a027",
                "serviceid": "0A4jXMx5TLV4q0zjn9AbrHzxaWWP2Kr3jTPhtKhnqUMHuW71wvJ4tGQUDHlnkrPX"
            },
            {
                "name": "Ice-Integration-V1",
                "_id": "5a8a79d727aacd44ab09be45",
                "serviceid": "0A4jXXOYkJIBdSnjSQ6pMjJfOvEBv9ayEa5ADTwEQcji7aCnTqT19VnqJnxagGNi"
            },
            {
                "name": "Try001",
                "_id": "5a8a99c827aacd44ab0a8860",
                "serviceid": "0A4k5oB4WmBhw7ZA5ElxdGKjLo0phhOwV0jiGNMbg4sZrIKSXOaaEDe0fm4W58x8"
            },
            {
                "name": "Ice-Integration-V2",
                "_id": "5a8baed527aacd44ab1481bd",
                "serviceid": "0A4otTWVgbKC06ywCwXnqVKMAuRscV3xzeJKdNmC4iGJgp3qYt75e1TAsOSnh5hj"
            },
            {
                "name": "sharedriveaccess",
                "_id": "5a8bb97b27aacd44ab15052f",
                "serviceid": "0A4p4qw4PDe3tgjN25bV8VwbPNCJq1arTmtMsOxgQjdvmR1PH1UATnGXkHGlntNQ"
            },
            {
                "name": "intakereq",
                "_id": "5a8bcfa927aacd44ab1559ff",
                "serviceid": "0A4pSjc1DLAM55LC1RmWJsBPU9Z1zxvjm61NhFAmIg1KWf3LoeoHWDXGuEBLHzvJ"
            },
            {
                "name": "StudentRegistration",
                "_id": "5a8bf1ff27aacd44ab165ec6",
                "serviceid": "0A4q3YmJBOk2x6THdSjZgZP8BwpOvewhSNqgv9oLqOsmZC3GagCdPeqdz1JsWsy6"
            },
            {
                "name": "studious",
                "_id": "5a8cf83027aacd44ab17e385",
                "serviceid": "0A4ubC8twY54QZqmLfKDpTttveYxdTNloqxgplacRsFL1QlJLvMJ6defRYmN1YL9"
            },
            {
                "name": "Alexaintegration-update",
                "_id": "5a8d21ab27aacd44ab18f497",
                "serviceid": "0A4vJk9Rc2I9Qagei2qVz8SAlPLrcde0f3OirIXf8HLObm4ycjDTDZLPoDCO96Oc"
            },
            {
                "name": "uitra",
                "_id": "5a8d4b9327aacd44ab19471e",
                "serviceid": "0A4w2kr3GgxpfkxWU6f7LH2KpdorQFXw6l2CJQODGgxTHJeKH90I2zejbfxFNIlL"
            },
            {
                "name": "time",
                "_id": "5a8d882327aacd44ab1a1223",
                "serviceid": "0A4x5oRGFgLetrwDpJhCgLvSn2900DAAiUKapbJfKYqDn7jmiJ65ruGIt4qwA48y"
            },
            {
                "name": "abcd",
                "_id": "5a8e40bc27aacd44ab1a3627",
                "serviceid": "0A50I4r0rpYi5MhC0KonYHrTwpEoKMpucE3YpdYwqoM07TzVfOSaJFblj9uotxY7"
            },
            {
                "name": "wallmart-train",
                "_id": "5a95035027aacd44ab29b377",
                "serviceid": "0A5UHYUAXcwo37ierkRkYY9im9qAMNwFDyF41WqOsgVQlWE8uoZ03SkuzdAlbln3"
            },
            {
                "name": "wallmart-train-1",
                "_id": "5a97a91e27aacd44ab32aeed",
                "serviceid": "0A5gZhqTJxEyRen2Lrj7AEBUlT4tQHGJbCrQndytQMlv0QUOjJlNGCa0hiclrduO"
            },
            {
                "name": "UTC",
                "_id": "5a9d67df27aacd44ab37054e",
                "serviceid": "0A65UrDGkp9bdoiI2DrRizhmfvxXcCV5sKrwxt3gbFl4ydgnDC1z5wH3ccdI1FQ1"
            },
            {
                "name": "KochiInfinity",
                "_id": "5a9e53fb27aacd44ab3c7c3b",
                "serviceid": "0A69aYHwB2DYQp3dMScGK4Rha8WZPmfCPW4iLqKEmQZysKXywgVPDJV45OaRNohc"
            },
            {
                "name": "SampleDemo",
                "_id": "5a3b3c3a4e0d078010485109",
                "serviceid": "09z45l2ZK3hCEaApGwEFpcDvhyMMqQVqt0xeBL28Gd7QQCqIjOU6A1FH6XddcGhs"
            },
            {
                "name": "NetAppChatBot",
                "_id": "5ab3775f35bf83edaa7bf273",
                "serviceid": "0A7fLF92K8BYLJaVwT7kPv6yU9eumO5WjwhzREHWgpKBmRFLAu0vklPp0Hs2ZICm"
            },
            {
                "name": "wolseley6",
                "_id": "5ab376d735bf83edaa7bdc05",
                "serviceid": "0A7fKYfrmy8VQcwSYgBHfQm28jN91it2yoA3YvuACjQg2wutkB9WA0MQZjWa1O1d"
            },
            {
                "name": "Yourhanes",
                "_id": "5ab3778e35bf83edaa7bfecd",
                "serviceid": "0A7fLXEVQs01zZRT1JZmaQZTUggeay5N7AbeOUBD5LCqYRi1xmIZEHO1C9O6dIuC"
            },
            {
                "name": "rajeev1",
                "_id": "5ab376b735bf83edaa7bdbf1",
                "serviceid": "0A7fKaKLbrKK1iiLmbIXm1dSayeigpl5IjpJ8LrZbZgyQeycIcTVOnzlCkiiKVr2"
            },
            {
                "name": "WalMart",
                "_id": "5ab4d8a9c9b8e8bacbcd5898",
                "serviceid": "0A7lSnRh0ghCE1JHNY6uQsJw6qmIHmzit4cvh0ID87vv7svcDc7csf46mvCO2pk8"
            },
            {
                "name": "HEBDescription",
                "_id": "5ab8cbb1c9b8e8bacbd2a41a",
                "serviceid": "0A82yqTGVNbCGnmdxtNBI9zloSkrqZxtZCJ3Q9rQBUrNKcA5UP1kzpGUAHRdjbqn"
            },
            {
                "name": "testboots1",
                "_id": "5ac8d1817d8ffd48937232e8",
                "serviceid": "0A9C2XwVaMPryhCgRjzUTwurJXIr8Q4i6YQqX8KmpayMInQlfQ1zyv4M8oKO0i0t"
            },
            {
                "name": "Walters-Kluer-Problem-Resolution",
                "_id": "5a3a5d0b4e0d07801047b14d",
                "serviceid": "09z0E3XGCXkus8CeZWDRW0HhmIkgdR2YeV0H9K5uLxEREvSma0LLkrEMMrIjwWAr"
            },
            {
                "name": "InteractionDemo",
                "_id": "5a8ba43627aacd44ab126844",
                "serviceid": "0A4oiMsWd0ZnRV4P8KeS2Uq7fBVIWvGOaHuFk3cZ7Scj1iw049U20PSyIUcBAGwM"
            },
            {
                "name": "FergusonBot",
                "_id": "5ab4d251c9b8e8bacbcd2069",
                "serviceid": "0A7lLqFuk4x55BKwupP0awp8CpzLP73gI3jhDYikCZ8B5DYygFO71PwiFZU9cEta"
            },
            {
                "name": "sample",
                "_id": "5add9fba460bbd27ed807b06",
                "serviceid": "0AAgJld0Hy8LfKZIh6W6GRz03DQv8VncAVHEdIixsFaIMiPWPo9pcBn9XglZCLHr"
            },
            {
                "name": "netapp-onproduction",
                "_id": "5b14e059003fe4047459a1fb",
                "serviceid": "0AEdNAZM6hU3WajGW4KOUmGDZlsxnAGSkviJDHSZNGOgZOJlpYef2Q2MemvAQqgB"
            },
            {
                "name": "Usecase1",
                "_id": "5ba4dcdf9667f708d2c2958e",
                "serviceid": "0AOvyvuRdXWxkZlLfHEmhFjFREsWQJ8MAg5E4fHrmtWVRkZSsCwjb2sJ7N5x6akI"
            },
            {
                "name": "mailtest",
                "_id": "5a13fed631121f93b725b7a2",
                "serviceid": "09wG3UM7EHbYQkgrX13FCi7gFyHfSbioL40tPpQWN5c2rHZpmI9JSkVeo0Thkxss"
            },
            {
                "name": "eeq",
                "_id": "5a18116f31121f93b7286e24",
                "serviceid": "09wY7NoSo9w9XQkVmZ0XdVb4iCLxMRweuHioE3VOPxZZkb1klD2zov2oXlecXwOd"
            },
            {
                "name": "justtesting",
                "_id": "5a26271f31121f93b72dc8cf",
                "serviceid": "09xYaTfQbM73Srwrq1VgN2vsiMenfQO6m7Rx8xQj38nWxMUTHXWTjdI1SbCLjWr2"
            },
            {
                "name": "WK-Digital",
                "_id": "5a584b2846b5b87be7ef63fd",
                "serviceid": "0A18yGM1wEvNBZxDhGUUWl0SVOj5uxZBlUcy0EolPB9D2nxKcYChmLYVELA6ogVu"
            },
            {
                "name": "UPSDemo",
                "_id": "5a702ac127aacd44abce2b0e",
                "serviceid": null
            },
            {
                "name": "Costco-category",
                "_id": "5a7d45c827aacd44abeb6e69",
                "serviceid": null
            },
            {
                "name": "Pizza",
                "_id": "5a850ae427aacd44ab0049e8",
                "serviceid": "0A4LRjIYUERzmETGptTjHbgvPmGlF1usz5OJYiNO8VyYh1IS4nIqDOvH6A384Mpw"
            },
            {
                "name": "testimport",
                "_id": "5a966f8427aacd44ab2f1319",
                "serviceid": null
            },
            {
                "name": "testboots",
                "_id": "5a96703927aacd44ab2fbae1",
                "serviceid": "0A5aavxP0I0dk8DRCVIIMVU3ES7K5g0d4brEIGwDl2G3Gd9LL9Gk6ok9H1v1w3ik"
            },
            {
                "name": "testForDemo",
                "_id": "59f96b85df0d8943fc6cef62",
                "serviceid": "09uMBhvwPEA3q62NoJkO3L1S8BkVpcx2enNeMC2f2Eu7tUwcghk53Z4M2RpMUXth"
            },
            {
                "name": "ggg",
                "_id": "5ae987979092520a8884aab3",
                "serviceid": "0ABX7bd6fskF2FaXqHUB5yfqumDI7Nr03EQ9j3aVw2EQfDxIuGzKoYgR9c0Yf2DO"
            },
            {
                "name": "BootsSalesOrderDemo",
                "_id": "5ac5c50738ee5ee2f5bb54a1",
                "serviceid": "0A8yWCDOtHG3xaXbBpywB6S71MFQ6T7Tv1fCnnBUWwUTTiSCBrbnVMhH8OKxIuMx"
            },
            {
                "name": "qwer",
                "_id": "5ac62c417d8ffd48936d13af",
                "serviceid": "0A90J7NtSxLpMBKxsG7JMX2vBCJNli1HvnbJYCoFyU6KwraHpCJQosyrZh0pveu1"
            },
            {
                "name": "INSURANCEASSISTANT",
                "_id": "5acafc807d8ffd4893778823",
                "serviceid": "0A9Lej7Dyebhlz8ZB6OqZGc4kK93vWH2gvsaS1QyCElY6Tvl5U30qrpGXjShQ9QP"
            },
            {
                "name": "Appstate",
                "_id": "5a17a77a31121f93b727b1cc",
                "serviceid": "09wWIdWOnGjx50O9PPftv5ILdIUuzCw6Pwam0lNxLsufqO84vzfQiryOlzbykEpV"
            },
            {
                "name": "state-street-test1",
                "_id": "5a31f8cefba8195fe960b61d",
                "serviceid": "09yP0XArK66DBJLegLNjgw2EBdMs8zV8k3NCxke7olRNHu9M2pNYmwGCMRpTraPe"
            },
            {
                "name": "ASDAvoicebot",
                "_id": "5aced201460bbd27ed6e20fd",
                "serviceid": "0A9cf87gggffaY8Y6cv74h36sPjml6Nnre8IkbX3eq6I3exZwm6Xk4kVJ4Vw664j"
            },
            {
                "name": "Vanguard",
                "_id": "5acee75c460bbd27ed6ed61b",
                "serviceid": "0A9d1wleW2C0jdqEXSTYLfGHOIOSbSY2Nr29SoUFnO7zMyv1zFEDVSb3zSF9eGvq"
            },
            {
                "name": "vanguardcharitable",
                "_id": "5acf08a1460bbd27ed6f053a",
                "serviceid": "0A9dc07hPVTuKHLafOKQ6l801SS8Kr3vAKPcYVa1iwEmGMY0x6JeCmvzUPMm4Js3"
            },
            {
                "name": "ASDAVOICEBOT2",
                "_id": "5acf2281460bbd27ed6f1e3e",
                "serviceid": "0A9e3VqFIEVcNub1jhIGzcDFEdUVLpzTQXuJdNlJyw23oFBzwlNHXjhKpnUyndQD"
            },
            {
                "name": "ATMASSISTANT",
                "_id": "5ad6d883460bbd27ed769a51",
                "serviceid": "0AACFr51p1F5Tm54YGmAc8g3Bq283w7C8PMOmaQwyIn2Amt55BOLUWcA2QRSfEDw"
            },
            {
                "name": "TROUBLESHOOTERASST",
                "_id": "5ad6e92a460bbd27ed76e775",
                "serviceid": "0AACXmANmdrjkoguEj1evRmQ41Vqe6UZckTaZUtORcR1oxVGJU8X673sQYZ0xXSL"
            },
            {
                "name": "RETAILASST",
                "_id": "5ad96d7a460bbd27ed7b3ad5",
                "serviceid": "0AANhpxmDLsuWEDWGPl4RqHrXEB0uFoBNOUnaPvvaQCuxAAuDypDhtXroZnnAty5"
            },
            {
                "name": "FINANACIALASST",
                "_id": "5ad9910a460bbd27ed7c6d02",
                "serviceid": "0AAOK8k5O2bRNmnt2G7FOgwlSpgr63uEnGde3sL70DMtGzlo9MwEATtL17K8WuqP"
            },
            {
                "name": "demobot",
                "_id": "5add988e460bbd27ed8041f3",
                "serviceid": "0AAgC3EkjmLDO4sUxqkS22TnUwylxz5PynXcBC4SfzXKlWbzjc8KNWJMnnz6NH9L"
            },
            {
                "name": "KGDemoIBMSpectrum",
                "_id": "5ae07272460bbd27ed833422",
                "serviceid": "0AAsqHsBDTpWseIgo0iWEVvfoVWAcdTmM0sOGZsn4pSnQ0KaRAaubiF9BLyqPoor"
            },
            {
                "name": "RPABluePrism",
                "_id": "5ae0c3d9460bbd27ed83b115",
                "serviceid": "0AAuFXLJJREXcuW81UWfggfpjHfXsAnSlBoeCwhL7VW4I5UCOPNOxgPCaY3OqvIN"
            },
            {
                "name": "BPProject",
                "_id": "5ae0ca9c460bbd27ed83ed07",
                "serviceid": "0AAuMjw3ELwsUt5uoWlrs6Yra5bJjzVdvkdh6IRuQqwIJlXIt3Lhzc6wunBydbV1"
            },
            {
                "name": "IBCCXAAnalysis",
                "_id": "5ae2e34c460bbd27ed8610cd",
                "serviceid": "0AB3fDGb1hWsSZmzyKO01NzFh7Xonj7c5BAwqoTHGJWYB1mJhaK10ORM5zxM0iKe"
            },
            {
                "name": "Infinityknowledge",
                "_id": "5ae94e8a9092520a88845a4f",
                "serviceid": "0ABW8URfNtoi8Ul2JtfCYDQxEjtpDJdGZSSIVV7qi1osGBvm5gZXiCbdpRlx0oHp"
            },
            {
                "name": "anthemtest",
                "_id": "5ae99dea9092520a8884e1a1",
                "serviceid": "0ABXVYF3b9IUD0tHU43SSa1tirlq4vvO8xBcyi86iuckxZaRfF0wZ38cSYqcynAe"
            },
            {
                "name": "SIPSolution",
                "_id": "5aea90559092520a888561da",
                "serviceid": "0ABbhxQGZcyjG2sgDBEBQD5naoXAOMAtyivTOysbcnAJEOHUN2XdlTHtLTQx51oi"
            },
            {
                "name": "SHOPPINGASST",
                "_id": "5ad9b180460bbd27ed7c7f1d",
                "serviceid": "0AAOt6O3nylb65ZRNKkcgskOxGx15gB6oqlt0gbBrY96l5eg87h504nws50oIazo"
            },
            {
                "name": "pdfExtraction",
                "_id": "5af0072921b1df0d645cba61",
                "serviceid": "0ABzwXrzCLMlpJNNDU3Lqmz8VB8uLSehacEiH85Z3WIO1lDJjEgwkxcfM8nSCQrO"
            },
            {
                "name": "train",
                "_id": "5af1827121b1df0d645fdfe3",
                "serviceid": "0AC6VvvkAucCXmtEPSQLR133olu5myuabxZ1tKvrlWUeBroxTojAMxJYjXfHMaKD"
            },
            {
                "name": "hhhh",
                "_id": "5af2ca6321b1df0d64632bf6",
                "serviceid": "0ACCCBNHEDGZVOcDJHaMTBPQ9olWEzuzLGnI1WtTYINPGxvmBxMPxJDhrAyteuQ3"
            },
            {
                "name": "deby",
                "_id": "5af29b1d21b1df0d6461e918",
                "serviceid": "0ACBNSTRTP36LAnDRLZE2rBOkYEM6yWwb2mK5O7xcDLx60cUBheICxYDx019pFvV"
            },
            {
                "name": "ticket",
                "_id": "5af3d25e21b1df0d6464cacf",
                "serviceid": "0ACGlkn8PZynRIv7vW5fEXhJ9DktcoNPueZea9kNg3KufApxkpVmTIndcVBLBahc"
            },
            {
                "name": "Next",
                "_id": "5af40b1b21b1df0d646599c9",
                "serviceid": "0ACHki2bTARmvboWIyEVyvNlZcOqZ2a8zjdy5aNVI34DdK7lKnPGQxPKajwmiFMT"
            },
            {
                "name": "incidentraising",
                "_id": "5af4387b21b1df0d646648c3",
                "serviceid": "0ACIXQIKKTbFkXd9kO74RDafJ3bnbeZlXOj5EhihEvCF7gSdZ5UdKJLTV89wYiye"
            },
            {
                "name": "demostudy",
                "_id": "5af51c1221b1df0d6476b20a",
                "serviceid": "0ACMTwCNiEfevyLOZ0IFp0t1ZRoiOb1cz4vejdJdYql8AQdBTDgGr6Wla25PBs1Z"
            },
            {
                "name": "AmishiD",
                "_id": "5af51d0721b1df0d6476bd7d",
                "serviceid": "0ACMUvNmKb0e98Hy4ghJU3oMu618EDKBRyRhXR39h6HGX3DXvPSvTIXdh0dJnkSR"
            },
            {
                "name": "TestProject",
                "_id": "5b07c2fb0e8e769cc4478088",
                "serviceid": "0ADhCs8UJXY6WqHLqDhB3brgRkZocsb4bFhzxhp9nT8A1IUT1CZHTHHtUpaA5qU3"
            },
            {
                "name": "LocationIdentifier",
                "_id": "5b0cfc130e8e769cc44e4d66",
                "serviceid": "0AE4N9NIe3Q1XC5lkExmLWHd1lYmWh73w3lg99JjFZNbbQdB8PAXpYbOcNbwsBDZ"
            },
            {
                "name": "UseCase2-Script",
                "_id": "5b0fcbad003fe404744f5fea",
                "serviceid": "0AEGq5FlhG6td1RygevXwYWbMG8kmYHygIFSSeQTqMxfUgbxOwE8SZPzorCugSLO"
            },
            {
                "name": "SampleProjectPrinter",
                "_id": "5b0fc9e2003fe404744f3945",
                "serviceid": "0AEGoZXDFaHSvEaW3ZCFOz0HcZLfrbqOUgYkYe3NpNjVZ7ykKpbVYMvmRRwvDIYr"
            },
            {
                "name": "EquifaxInc-Bot",
                "_id": "5b14ca6b003fe40474578fed",
                "serviceid": "0AEczcaRUZXkVUTgHKUSPvdsWg9haAh9HI2LjkTnqcsNKDCvd1s4WwLfn398ktuI"
            },
            {
                "name": "Nissan",
                "_id": "5ac4ac5138ee5ee2f5b90b59",
                "serviceid": "0A8tejkt0yhhSehjq9uG6hUI0TETxf2fc1Pnq8kQwSDCXsisSejd8yxsAMgLIOO5"
            },
            {
                "name": "SampleSkillSearch",
                "_id": "5b1601dc003fe404745ff082",
                "serviceid": "0AEiOBaWbmDOj11WRbEAlADkBsbP90JdBAU9XrhsidSk6JAMi6a3Qa3R8wgTkt9G"
            },
            {
                "name": "retailusecase123",
                "_id": "5b1a231b003fe404747309cf",
                "serviceid": "0AF0hmLZgv30cgTBBDcPIVNxTDNjNiI0nuCB6C6qGVoc9ngDYbvLq09rhuLWwnvf"
            },
            {
                "name": "HRBot",
                "_id": "5b1df7fee918780a05a9ba6d",
                "serviceid": "0AFHjKAAI8hLnailwc85QNdoTzUKqrjCUMxqEuOd7anIGQzXZ4kuKxtgzCiHtalc"
            },
            {
                "name": "MychatApp",
                "_id": "5b1df9d7e918780a05aa29f4",
                "serviceid": "0AFHjgiqwpUu0MKT1aYwSVnvx5WIvfspI7qR0t10oO1Z4AAquoXQnORrt3gB6S0Z"
            },
            {
                "name": "Skv123",
                "_id": "5b1dfe21e918780a05aa900b",
                "serviceid": "0AFHo5jIfZcVLjSNjolvAzMne4vnbf8jOjXmSOofFDKyqDc1aZvaa8i6GvlZgUGw"
            },
            {
                "name": "TravelBooking",
                "_id": "5b1df868e918780a05a9c0b1",
                "serviceid": "0AFHjKR4Ge2vz3ZweKuuR1zsm8zYQIum9gTKgt2BznWL3LZoUkiZwstdNiiizZMq"
            },
            {
                "name": "hrchatbot",
                "_id": "5b1df9dee918780a05aa2a03",
                "serviceid": "0AFHjdItupKI9N3NIm9ntKsDT7UoKUAPbxerQ5gVtfYyw8IepBYiWmzHzRLzyRo1"
            },
            {
                "name": "sampledemo",
                "_id": "5b1dfb82e918780a05aa4b25",
                "serviceid": "0AFHlIKmyFV0MkR1JkxtL16wRxhLN6fH6lblqzypAXHbgjABTvjr3WAE6QMelYVm"
            },
            {
                "name": "LoanCalcBot",
                "_id": "5b1e36b1e918780a05ae2dd8",
                "serviceid": "0AFImlyN03mvsuQu1G9suOn1ZdD9tpnUEPOXbUh6wfBvjjTlA5nHogJmI18dkW6T"
            },
            {
                "name": "POCChatbot",
                "_id": "5b1fa629e918780a05b248e6",
                "serviceid": "0AFP9oEJYCL9BhqNgudYdFPhPVWySmdc1C2e07Vj6lxfUkUbncIA2i5OGSGOcW3G"
            },
            {
                "name": "AsstForDiscover",
                "_id": "5a68b82327aacd44abc88c8d",
                "serviceid": "0A2Jp1W9ROc904ZHKssL7MWjLfe3d2VBzLZjserGZCeMmV9QcSTuKQ6CDUsPu6eb"
            },
            {
                "name": "kochitest",
                "_id": "5b30723bd15aba2c9d46caef",
                "serviceid": "0AGbeaUIgG5IoNHSB6v8bRHeCDQgpPV2uGsBQkEpkdunWA8Mj7QJs1Ye0y5QRUWI"
            },
            {
                "name": "princessbot",
                "_id": "5b30725fd15aba2c9d46cb03",
                "serviceid": "0AGbejcRj7CF4I5O6NO7nPsp3lr4HrLAQHxaLMYIDdHUhpDGCDvODTwQd8YjTThi"
            },
            {
                "name": "Netapp-Quoteedge",
                "_id": "5b3476a935b90f0977445b6c",
                "serviceid": "0AGtT7VzQVL83sQsLmhc5u8gIXZaEd5sJ5bEF3RAV0GYKyov6RfVBuMWGZiyIxBN"
            },
            {
                "name": "test-10",
                "_id": "5b443e164374de092df8ef1a",
                "serviceid": "0AI1T4kBnREJAgLfFrNQk58yEciZ6uDaBQXqC0yjMzYwbIbkYORgiSUZDpq0EQ88"
            },
            {
                "name": "boots-test",
                "_id": "5b4593ecdae133096329ad10",
                "serviceid": "0AI7NC0iEcOrucipM5TsLCfCY1c7Hhb2WHGYDa3Z7Rj8V26LGgCXX5pb452tKv8Q"
            },
            {
                "name": "BootsProducts",
                "_id": "5b4c5e9cc9a9b809e1378b2e",
                "serviceid": "0AIbV3jtdyFIf7MrM7coZqfGyHREdVeNakHs4USlFXsuxTYQ3w83YWg3CE5lWxTb"
            },
            {
                "name": "Anoop-Test",
                "_id": "5b55651ac9a9b809e1412e3a",
                "serviceid": "0AJFWkMqpIzNo0F7nsbXsVJxBLDz6Jj6sMOiBFKLjEB36106iG7nsj2tWYvb0yXV"
            },
            {
                "name": "MessageIndicator",
                "_id": "5b55a419c9a9b809e143fe97",
                "serviceid": "0AJGcJOP4kGYwQ4mo9tbJraCy7SOYyTUSUwaKJR4evLFWKGlGcvJif9ygcDqlhhQ"
            },
            {
                "name": "MessageSeverityCalculator",
                "_id": "5b55afe4c9a9b809e1452dc0",
                "serviceid": "0AJGozK6V4rLt0f2xofk6rBVA8jB7W9RdUdUJ0N3LqObuJFecBcpR8Mjh3CJhRyz"
            },
            {
                "name": "TestResetPassword",
                "_id": "5b55bfbac9a9b809e1476d95",
                "serviceid": "0AJH6SUu801nhMeaNN6NG0WzFYnT8NrU7gL30aFqgOiPYHaQtcxWcLz6aFeCFhx3"
            },
            {
                "name": "UserValidationPOC",
                "_id": "5b55c2b9c9a9b809e147f9e5",
                "serviceid": "0AJH9HfTA6oPek72MN21Nt01nxXY494Y1iBt518sla5LuZwG9H33ZqWZeVJ8YJg6"
            },
            {
                "name": "AVA",
                "_id": "5b61754b359c7f24178a2941",
                "serviceid": "0AK71tXPK2DdOD8hqIdfy1fTDz5TaRMdwcbB95aYdHdXLDQv4JtmyihH6P6PL21a"
            },
            {
                "name": "Test-ava",
                "_id": "5b6bf622359c7f241796858c",
                "serviceid": "0AKrc4KzG8WwJaHrDS0OQA2AxQYT0LOZQKbQRyuXTDXNZNiDFQR2FN6HFu0qMEji"
            },
            {
                "name": "VehiclePass",
                "_id": "5b6d6b8b359c7f241798ce17",
                "serviceid": "0AKy5Mgm6Zz4HynBGjstC66l8lNQuX53GaSwK7hNspn1VOfRwSa2ZjmnvxCHHDd8"
            },
            {
                "name": "LeaveRequest",
                "_id": "5b6d76c3359c7f24179968ba",
                "serviceid": "0AKyHHVB3HYLGFYXPqH5fsxLjceB3W8lMdaKTpMkW5DxCqdajHQJDTQWFNazrQYO"
            },
            {
                "name": "MedicalAssistant-septTest",
                "_id": "5b861fa9359c7f2417c9c805",
                "serviceid": "0AMjeDSeou3ll2FVOfBJchJaAYzT90W9iS7c4PWR7qVhNm8t1FCZEdf8Wj2N8uUx"
            },
            {
                "name": "Sample",
                "_id": "5b88cc41359c7f2417d364df",
                "serviceid": "0AMvVXQxCbPCbMA6fNUSwJAuSFFt8yBhd7dbexSDotA618vsZev2t5vxBWF3vVE4"
            },
            {
                "name": "EquifaxPoc",
                "_id": "5b8fbe81359c7f2417e7cc40",
                "serviceid": "0ANQJfo3GPCP8ss9VkIzNgmrugBdW2ExZERsubnxxhD12HvwssaRgYzmHnbE8p5Y"
            },
            {
                "name": "travelling",
                "_id": "5ba0f5959667f708d2bc6595",
                "serviceid": "0AOefVlJqt59m1GeNSfawsxs1SsUJgmNfceVCI0N3xzxYHor5nUpE2zyMUDOhTvA"
            },
            {
                "name": "Sample-client",
                "_id": "5bb5e13dfc5bf10962417c18",
                "serviceid": "0AQ9SLf2BmyZiKtyOotoSQebZjEe3COkQZBkBgMjuGcPNKlmHJ6pgaTPgoRArzRM"
            },
            {
                "name": "Test-Vodafone",
                "_id": "5bbc62f9fc5bf10962469f59",
                "serviceid": "0AQcK6TvA5B2se1uIb3YEC8NxmszKtFZoPytYfcCtcgxFldb2X2WswGEMXaJK1CC"
            },
            {
                "name": "NETAPP-ORIENTDB",
                "_id": "5bbddf8ae516fe0a3be08bc5",
                "serviceid": "0AQiuJkEp73lEtTi2I0zASackhhi9UrCiDKDYX7MOb1YRHIjUVvgnGTFxWKCgO7W"
            },
            {
                "name": "vodafoneorderrequest",
                "_id": "5bbeea90e516fe0a3be4a4cd",
                "serviceid": "0AQnX9ZqEblQnmXkXIEGXmouDdHKAFgmhzGjbr62pkfto3fjdRKmKLuvvxeUGozv"
            },
            {
                "name": "netapp-test-cz-testplan",
                "_id": "5bbeffafe516fe0a3be63bc9",
                "serviceid": "0AQntpgjNxVJXS529qzCET0uSEleN6wpGRUjAno9dQAaMUnA789fnv1KLpcK842W"
            },
            {
                "name": "RajVodafone",
                "_id": "5bbf2209e516fe0a3bf01a28",
                "serviceid": "0AQoUjOn0IyKVdb0vJ4WKYKGmOpQIi7PUm7WoUyXmTWNyW234ReakSJzhG5xGg5z"
            },
            {
                "name": "KG-Test",
                "_id": "59f1675adf0d8943fc6b4c4e",
                "serviceid": "09tmdMS7eKYnRmHVciGKGYzLXm4cVXJK8OMzLw9fhI2WVIB7hU7oGWQ8UI7OsRrR"
            },
            {
                "name": "SreekanthcTest",
                "_id": "59f96ba1df0d8943fc6cf641",
                "serviceid": "09wL252AOH41qZn5WE8pq9s7zbxOd3OVWZshLb0fJNXbxuCLqQvt3nJQ3pPEwUoM"
            },
            {
                "name": "testTravel",
                "_id": "59e83e56df0d8943fc69867d",
                "serviceid": "09t80SEDNYfIykLoxhypsF7MfoWCoilUtSRTGA1nEB7HKR7cWAzAWX5UpH8c1O4J"
            },
            {
                "name": "WaltersKluwer-KB",
                "_id": "5a3a24af66dc04cc378c76d6",
                "serviceid": "09yzFnpaaZe1G11CsuxhqM0pTAQkoYiiBV6SCOdCfvR2wt7sZ2gDHoVyU6OVEvrx"
            },
            {
                "name": "speechToText",
                "_id": "5a5ee41327aacd44abb79b10",
                "serviceid": "0A1cEOHFhGIF4G4PuE6NxJ6CIQZ2jjB74TKfNP4wDtgD2UqAdmfHWuKlqubNL557"
            },
            {
                "name": "varunust",
                "_id": "5a74042327aacd44abd8e20a",
                "serviceid": "0A37vvNYSLMJEbWhGKjxZeWyoTSr9s3VCwjR9sAMOxXON0ZZuweRb9BKG92rsPsb"
            },
            {
                "name": "demozxc",
                "_id": "5a83e21227aacd44abfd8ea7",
                "serviceid": "0A4GIdcXfA9DEt6wW1chRGk3iJsprB7haT79RrO6ABroZugkCwiNMgRrcJhsrb3N"
            },
            {
                "name": "testapp",
                "_id": "5ab3478335bf83edaa78b88c",
                "serviceid": "0A7eVqg0XxNpUwFnFqh61SKMqgrghFRAnAs4nxpFFCc0GWz65aRDAyxclGyNf2h0"
            },
            {
                "name": "TableBooking",
                "_id": "5b1df926e918780a05a9eb95",
                "serviceid": "0AFHjQERuXCQaRmDNmCemxo2BfXAjRcdvTNoA6ZYhZL2EuGGt0dnsxvBqqLD7G7g"
            },
            {
                "name": "Sam",
                "_id": "5b1fa65ce918780a05b24ca2",
                "serviceid": "0AFP9hvh052WqYAvymDxUbKECAQhQNuzPHEd5nAdlUOkcFXVpGQUx812vUgYncet"
            },
            {
                "name": "Demo",
                "_id": "5b07a1630e8e769cc44706ca",
                "serviceid": "0ADgdJOgEaBaiPqYxGIzGhaFYg55ocViqyrNfHMuh7DsW6WHkZwvrkZKEybiidwm"
            },
            {
                "name": "Sempra-MCS-POC",
                "_id": "5bd2f522a973d070442b028b",
                "serviceid": "0ASEQ83TIiQ51xdCFjtfhxXpFJsFlgmErQ0vAPvZ7k3P7hy7o3RjbDcJ1LW7uSxT"
            },
            {
                "name": "sample-newClient",
                "_id": "5bd823a5a973d0704433a7a6",
                "serviceid": "0ASbP03JOX80CUzGmylORKQCR8a6HPvbtzUmYrImx2vFSPV7BzE8SNg1oiwpT0Vg"
            },
            {
                "name": "Ashley-Alexa",
                "_id": "5be3d27335df3a6bd5c06c68",
                "serviceid": "0ATRDZTZTk24MugYeadDsyO8f1VF7z8oLUgMq9MLOAScmvTqA0Ju2dPhwqP1N9K4"
            },
            {
                "name": "coffee",
                "_id": "5be3d4a835df3a6bd5c07c27",
                "serviceid": "0ATRFwOKYEq2wRy4Lz3tmFDcxNOhLj723wsSOqFFL4i89WVIxDJgxQixEb73pr2P"
            },
            {
                "name": "DemoAisleLocator",
                "_id": "5beaf0ed35df3a6bd5cdff4d",
                "serviceid": "0ATwnBkI17niK6J2vcHBXkDZvpWyn230ZG1SXlpZBFnsGzhFCiKOLH5KtBylvzck"
            },
            {
                "name": "healthcareproD3",
                "_id": "5c027b6b35df3a6bd5110f4d",
                "serviceid": "0AVdCXV59yltZX4lCAvf4FQ1tzXH85gSUXNvjv84AMkpEzkWpIRSHYCHJhrjOUYT"
            },
            {
                "name": "IceTetsing",
                "_id": "5c076fff35df3a6bd5239bd9",
                "serviceid": "0AVzBBMXY9B5eiJlRRDFI9z5rZiqnBPJYoUuq3jGvF1hlw5wZsdpbSMrd24X70Sj"
            },
            {
                "name": "Retail-chatbot",
                "_id": "5c1089fe35df3a6bd53653d4",
                "serviceid": "0AWdXwvmvJ695pjnVfPNsW6Bbhk8iRG6RMPD1jt4ZJ8Ff8xz6XUzLvjEUCQicono"
            },
            {
                "name": "RetailChatbot",
                "_id": "5c109e0835df3a6bd537104c",
                "serviceid": "0AWdtUevsLcco5MiYRK8mG01xE665uSVhi9m7Rx9HRV3BYKDMgYuRdegn6IS2rtM"
            },
            {
                "name": "RetailChat",
                "_id": "5c109ff335df3a6bd5372b47",
                "serviceid": "0AWdvX6iqjaNrd7ndd2IUgMzlXtrcigKRHIg9s3loqtpuK3fC5WuOw7vlR6pgbsf"
            },
            {
                "name": "excite-chatbot",
                "_id": "5bfacb1a35df3a6bd5efc548",
                "serviceid": "0AV56GzXT4347eChrwdc5UTfKWw5S9zLF4NjN9gPco51A7AqbOBqbs08B0xAPf38"
            },
            {
                "name": "Fabtemp",
                "_id": "5c122a6635df3a6bd5417804",
                "serviceid": "0AWklEZ0UJbKxd6vWv6R8zNA0LjySHei8PrfYZgzS9UjCKIfqsYrRHe87FwZG1fD"
            },
            {
                "name": "ProductMentions",
                "_id": "5c2c941f6594a8026ca84a09",
                "serviceid": "0AYduKy3dKoF3UISVIIYx8pD2V6Rzb0FAmiJehQLlNxtsLInBXeRNUr2B0R4CD2C"
            },
            {
                "name": "HPS",
                "_id": "5c35d9b36594a8026cbcb59d",
                "serviceid": "0AZJ1uiH8CIdIV3XgHvuLPdTbqHJcUZ6igOiSocgHsKsoKUPEsebsZotuiR7Tauj"
            },
            {
                "name": "emai-pdf",
                "_id": "5c3721eb6594a8026cc104df",
                "serviceid": "0AZOiTtDTY59lu84LOP9aFCYdFKJvegDbY0JIrAdcg1QmgNU3unMcFPCugtHhSIL"
            },
            {
                "name": "Cigna-CheckBox",
                "_id": "5cc6f09e6e081837531772d2",
                "serviceid": "0AjgWygZAvwiKFyuWIHcOWrIfr51kGQ1uPnJpBIB9zTYeYVoxPOe76vVEZ8N3Dux"
            },
            {
                "name": "Cigna-ListCheck",
                "_id": "5ccaacb56e081837532661c0",
                "serviceid": "0Ajx5xVYSKfHsKLP6Tl21pBV4P6eWNb4z32zISKeGqRtRScigChHtA3lB1VksHMJ"
            },
            {
                "name": "InfyDemoForTest1",
                "_id": "5cd1532e6e081837536bb2d2",
                "serviceid": "0AkQafkXwiNNFRCpc2h9ubbmUi21kooRtm3vSlXjsObt3L4bkCKsNPGzpURViNKv"
            },
            {
                "name": "BuyBot",
                "_id": "5cd8fe266e081837539656d4",
                "serviceid": "0AkybBxM3Vg78xaeDl4KEhEPDkbLlF2LcrmV1OUdHaExlJh9xjX3PiBi0WJmkvPt"
            },
            {
                "name": "travelservice",
                "_id": "5a057b42c8435ee1bc9f7cc1",
                "serviceid": "09vUepTxOIz3RokD6MC7IcGByhbRaVOIXdS4W0n7Jmzf4CAkVnPANJlsQpKbwEnl"
            },
            {
                "name": "myConfidenceBuilder",
                "_id": "5a6eb75227aacd44abca5e9e",
                "serviceid": "0A2kQ3TfuRgChACrpYzAjG9b7EoKubUIC05YrTzlTy5ibeQpZo3AFZhxjnfVA9DC"
            },
            {
                "name": "botsample101",
                "_id": "5a815d7c27aacd44abf2726e",
                "serviceid": "0A458GdWlEjYrqLEUPRBya5JiMRymbnaH4JWlqX4O1sJF5TvXe26BbPf0sEZEmUA"
            },
            {
                "name": "DhanChat",
                "_id": "5a81982627aacd44abf4fac3",
                "serviceid": "0A469E6jml7M9E0cCpe9chp3K5Lsuf34OGG12vc9FBdkQ7M6kZ61jsiXkDglTXsX"
            },
            {
                "name": "Travel-PlannerApp",
                "_id": "5a8b905127aacd44ab123dbc",
                "serviceid": "0A6HtGHSGdFZgF1rDRll06Ldu3OIkmr6oOCSsTMFKZ47wSdqT8ZKmhdYR4xMvBfI"
            },
            {
                "name": "priceChatBot",
                "_id": "5b1df856e918780a05a9c0a9",
                "serviceid": "0AFHifSLSBtJfHPdXlNEJofUHkID0EOZoAiC5p5cltpuSI4xp7ALSj7qbPu7wCSn"
            },
            {
                "name": "CareMoreCheckin-V5",
                "_id": "5cf502c2308aae6a117c0243",
                "serviceid": "0AmyreYioFkLYvlYoEd9NWCmxt99fiu4I3m3J6x717z65u3y8jjlA95fZoakKQR1"
            },
            {
                "name": "WalmartPOC",
                "_id": "5d1307e1144b3514032447e6",
                "serviceid": "0Ap80dPbiZhtJ093Gfk160FtiaJJWD2QA0EFXScbGm6ReKYZo2oSLOOK71OBDlGd"
            }
        ]
    }
}

#######################################################################################################################
Import Projects:

Query:
query
 GetDataSourceConfig($id0:ID!,$id1:ID!,$id2:ID!,$id3:ID!){import0:projectconfigs(project:$id0){

      ...projectFields

   }import1:projectconfigs(project:$id1){

      ...projectFields

   }import2:projectconfigs(project:$id2){

      ...projectFields

   }import3:projectconfigs(project:$id3){

      ...projectFields

   }}

   fragment projectFields on ProjectConfig {

         datasource{

           serviceid

           utterances{

             utterance

             case_converted_utterance

             mapping

             ir_trained

             ner_trained

           }

           entities

           intents{

             name

             description

             createdAt

             modifiedAt

           }

           patterns{

             pattern

             entity

           }

           phrases{

             phrase

             entity

           }

           synonyms{

             synonym

             word

           }

         }

   } 

Request URL:
http://ice-xd.southindia.cloudapp.azure.com:3001/project/manage

POST Data:
{"id0":"5952a1a1c9c57fd148d088eb","id1":"5965bcb2c9c57fd148d08c4a","id2":"5965a976c9c57fd148d08b8f","id3":"5979a4d7fc97be6468dbfd1c"}
5952a1a1c9c57fd148d088eb, 5965bcb2c9c57fd148d08c4a, 5965a976c9c57fd148d08b8f, 5979a4d7fc97be6468dbfd1c are the project ids.

JSON Response:
{
    "data": {
        "import0": [
            {
                "datasource": {
                    "serviceid": "09iQSyU0GQ1qzKq7HJ8a89Bs52nYmD36JcuTyl373O7fbgmYov6NmXqmN8RiL2yJ",
                    "utterances": [
                        {
                            "utterance": "1234 ",
                            "case_converted_utterance": "1234 ",
                            "mapping": "{\"tokens\": [\"1234\"], \"intent\": \"OTP\", \"tags\": []}",
                            "ir_trained": true,
                            "ner_trained": true
                        },
                        {
                            "utterance": "Otp is 1234 ",
                            "case_converted_utterance": "Otp is 1234 ",
                            "mapping": "{\"tokens\": [\"Otp\", \"is\", \"1234\"], \"intent\": \"OTP\", \"tags\": []}",
                            "ir_trained": true,
                            "ner_trained": true
                        },
                        {
                            "utterance": "My card is 1234-1234-1234 ",
                            "case_converted_utterance": "My card is 1234-1234-1234 ",
                            "mapping": "{\"tokens\": [\"My\", \"card\", \"is\", \"1234-1234-1234\"], \"intent\": \"reset\", \"tags\": [{\"start\": 3, \"tag\": \"card\", \"end\": 4, \"entity\": \"1234-1234-1234\"}]}",
                            "ir_trained": true,
                            "ner_trained": true
                        },
                        {
                            "utterance": "My card is trapped in the ATM ",
                            "case_converted_utterance": "My card is trapped in the ATM ",
                            "mapping": "{\"tokens\": [\"My\", \"card\", \"is\", \"trapped\", \"in\", \"the\", \"ATM\"], \"intent\": \"reset\", \"tags\": []}",
                            "ir_trained": true,
                            "ner_trained": true
                        },
                        {
                            "utterance": "hi",
                            "case_converted_utterance": "hi",
                            "mapping": "{\"tokens\": [[\"hi\", 0]], \"text\": \"hi\", \"intent\": \"Greeting\", \"id\": 0, \"tags\": []}",
                            "ir_trained": true,
                            "ner_trained": true
                        },
                        {
                            "utterance": "hello",
                            "case_converted_utterance": "hello",
                            "mapping": "{\"tokens\": [[\"hello\", 0]], \"text\": \"hello\", \"intent\": \"Greeting\", \"id\": 1, \"tags\": []}",
                            "ir_trained": true,
                            "ner_trained": true
                        },
                        {
                            "utterance": "Good morning",
                            "case_converted_utterance": "Good morning",
                            "mapping": "{\"tokens\": [[\"Good\", 0], [\"morning\", 5]], \"text\": \"Good morning\", \"intent\": \"Greeting\", \"id\": 2, \"tags\": []}",
                            "ir_trained": true,
                            "ner_trained": true
                        },
                        {
                            "utterance": "how are you",
                            "case_converted_utterance": "how are you",
                            "mapping": "{\"tokens\": [[\"how\", 0], [\"are\", 4], [\"you\", 8]], \"text\": \"how are you\", \"intent\": \"Greeting\", \"id\": 3, \"tags\": []}",
                            "ir_trained": true,
                            "ner_trained": true
                        },
                        {
                            "utterance": "bye",
                            "case_converted_utterance": "bye",
                            "mapping": "{\"tokens\": [[\"bye\", 0]], \"text\": \"bye\", \"intent\": \"Goodbye\", \"id\": 4, \"tags\": []}",
                            "ir_trained": true,
                            "ner_trained": true
                        },
                        {
                            "utterance": "good bye",
                            "case_converted_utterance": "good bye",
                            "mapping": "{\"tokens\": [[\"good\", 0], [\"bye\", 5]], \"text\": \"good bye\", \"intent\": \"Goodbye\", \"id\": 5, \"tags\": []}",
                            "ir_trained": true,
                            "ner_trained": true
                        },
                        {
                            "utterance": "see you later",
                            "case_converted_utterance": "see you later",
                            "mapping": "{\"tokens\": [[\"see\", 0], [\"you\", 4], [\"later\", 8]], \"text\": \"see you later\", \"intent\": \"Goodbye\", \"id\": 6, \"tags\": []}",
                            "ir_trained": true,
                            "ner_trained": true
                        },
                        {
                            "utterance": "Could you reset the ATM PIN",
                            "case_converted_utterance": "Could you reset the ATM PIN",
                            "mapping": "{\"tokens\": [[\"Could\", 0], [\"you\", 6], [\"reset\", 10], [\"the\", 16], [\"ATM\", 20], [\"PIN\", 24]], \"text\": \"Could you reset the ATM PIN\", \"intent\": \"reset\", \"id\": 7, \"tags\": [{\"start\": 4, \"tag\": \"ATMPIN\", \"end\": 6, \"entity\": \"ATM PIN\"}]}",
                            "ir_trained": true,
                            "ner_trained": true
                        }
                    ],
                    "entities": [
                        "ATMPIN",
                        "card"
                    ],
                    "intents": [
                        {
                            "name": "Greeting",
                            "description": "Greeting",
                            "createdAt": "2018-10-25T09:21:34.087Z",
                            "modifiedAt": "2018-10-25T09:21:34.087Z"
                        },
                        {
                            "name": "Goodbye",
                            "description": "Goodbye",
                            "createdAt": "2018-10-25T09:21:34.087Z",
                            "modifiedAt": "2018-10-25T09:21:34.087Z"
                        },
                        {
                            "name": "reset",
                            "description": "reset",
                            "createdAt": "2018-10-25T09:21:34.087Z",
                            "modifiedAt": "2018-10-25T09:21:34.087Z"
                        },
                        {
                            "name": "OTP",
                            "description": "OTP",
                            "createdAt": "2018-10-25T09:21:34.087Z",
                            "modifiedAt": "2018-10-25T09:21:34.087Z"
                        },
                        {
                            "name": "atm",
                            "description": "atm",
                            "createdAt": "2018-10-25T09:21:34.087Z",
                            "modifiedAt": "2018-10-25T09:21:34.087Z"
                        },
                        {
                            "name": "No intent",
                            "description": "no intent",
                            "createdAt": "2018-10-25T09:21:34.087Z",
                            "modifiedAt": "2018-10-25T09:21:34.087Z"
                        }
                    ],
                    "patterns": [],
                    "phrases": [
                        {
                            "phrase": [
                                "Chrome Card",
                                "Discover it Card"
                            ],
                            "entity": "product"
                        }
                    ],
                    "synonyms": []
                }
            }
        ],
        "import1": [
            {
                "datasource": {
                    "serviceid": "09jnCMpx2xQEFeVB3HEn8hUnJKMTEvmNymp8x66ji5CO86QrgvCIwWZRo9nGY1gY",
                    "utterances": [
                        {
                            "utterance": "Hi ",
                            "case_converted_utterance": "Hi ",
                            "mapping": "{\"tokens\": [\"Hi\"], \"intent\": \"intro\", \"tags\": []}",
                            "ir_trained": true,
                            "ner_trained": true
                        },
                        {
                            "utterance": "i want to open a savings account",
                            "case_converted_utterance": "i want to open a savings account",
                            "mapping": "{\"tokens\": [[\"i\", 0], [\"want\", 2], [\"to\", 7], [\"open\", 10], [\"a\", 15], [\"savings\", 17], [\"account\", 25]], \"text\": \"i want to open a savings account\", \"intent\": \"openAccount\", \"id\": 0, \"tags\": [{\"start\": 5, \"tag\": \"account\", \"end\": 7, \"entity\": \"savings account\"}]}",
                            "ir_trained": true,
                            "ner_trained": true
                        },
                        {
                            "utterance": "i want to open an FD",
                            "case_converted_utterance": "i want to open an FD",
                            "mapping": "{\"tokens\": [[\"i\", 0], [\"want\", 2], [\"to\", 7], [\"open\", 10], [\"an\", 15], [\"FD\", 18]], \"text\": \"i want to open an FD\", \"intent\": \"openAccount\", \"id\": 1, \"tags\": [{\"start\": 5, \"tag\": \"account\", \"end\": 6, \"entity\": \"FD\"}]}",
                            "ir_trained": true,
                            "ner_trained": true
                        },
                        {
                            "utterance": "I want to apply for loan",
                            "case_converted_utterance": "I want to apply for loan",
                            "mapping": "{\"tokens\": [[\"I\", 0], [\"want\", 2], [\"to\", 7], [\"apply\", 10], [\"for\", 16], [\"loan\", 20]], \"text\": \"I want to apply for loan\", \"intent\": \"applyLoan\", \"id\": 2, \"tags\": [{\"start\": 5, \"tag\": \"loan\", \"end\": 6, \"entity\": \"loan\"}]}",
                            "ir_trained": true,
                            "ner_trained": true
                        },
                        {
                            "utterance": "what are the steps to open a new account",
                            "case_converted_utterance": "what are the steps to open a new account",
                            "mapping": "{\"tokens\": [[\"what\", 0], [\"are\", 5], [\"the\", 9], [\"steps\", 13], [\"to\", 19], [\"open\", 22], [\"a\", 27], [\"new\", 29], [\"account\", 33]], \"text\": \"what are the steps to open a new account\", \"intent\": \"openAccount\", \"id\": 3, \"tags\": [{\"start\": 8, \"tag\": \"account\", \"end\": 9, \"entity\": \"account\"}]}",
                            "ir_trained": true,
                            "ner_trained": true
                        },
                        {
                            "utterance": "how to open a SB account",
                            "case_converted_utterance": "how to open a SB account",
                            "mapping": "{\"tokens\": [[\"how\", 0], [\"to\", 4], [\"open\", 7], [\"a\", 12], [\"SB\", 14], [\"account\", 17]], \"text\": \"how to open a SB account\", \"intent\": \"openAccount\", \"id\": 4, \"tags\": [{\"start\": 4, \"tag\": \"account\", \"end\": 6, \"entity\": \"SB account\"}]}",
                            "ir_trained": true,
                            "ner_trained": true
                        },
                        {
                            "utterance": "what is the rate of interest of a housing loan",
                            "case_converted_utterance": "what is the rate of interest of a housing loan",
                            "mapping": "{\"tokens\": [[\"what\", 0], [\"is\", 5], [\"the\", 8], [\"rate\", 12], [\"of\", 17], [\"interest\", 20], [\"of\", 29], [\"a\", 32], [\"housing\", 34], [\"loan\", 42]], \"text\": \"what is the rate of interest of a housing loan\", \"intent\": \"applyLoan\", \"id\": 5, \"tags\": [{\"start\": 8, \"tag\": \"housingLoan\", \"end\": 10, \"entity\": \"housing loan\"}]}",
                            "ir_trained": true,
                            "ner_trained": true
                        },
                        {
                            "utterance": "how can i take a car loan",
                            "case_converted_utterance": "how can i take a car loan",
                            "mapping": "{\"tokens\": [[\"how\", 0], [\"can\", 4], [\"i\", 8], [\"take\", 10], [\"a\", 15], [\"car\", 17], [\"loan\", 21]], \"text\": \"how can i take a car loan\", \"intent\": \"applyLoan\", \"id\": 6, \"tags\": [{\"start\": 5, \"tag\": \"carloan\", \"end\": 7, \"entity\": \"car loan\"}]}",
                            "ir_trained": true,
                            "ner_trained": true
                        }
                    ],
                    "entities": [
                        "account",
                        "loan",
                        "housingLoan",
                        "carloan"
                    ],
                    "intents": [
                        {
                            "name": "openAccount",
                            "description": "openAccount",
                            "createdAt": "2018-10-25T09:21:34.091Z",
                            "modifiedAt": "2018-10-25T09:21:34.091Z"
                        },
                        {
                            "name": "applyLoan",
                            "description": "applyLoan",
                            "createdAt": "2018-10-25T09:21:34.091Z",
                            "modifiedAt": "2018-10-25T09:21:34.091Z"
                        },
                        {
                            "name": "Welcome Message",
                            "description": "Welcome Message",
                            "createdAt": "2018-10-25T09:21:34.091Z",
                            "modifiedAt": "2018-10-25T09:21:34.091Z"
                        },
                        {
                            "name": "intro",
                            "description": "intro",
                            "createdAt": "2018-10-25T09:21:34.091Z",
                            "modifiedAt": "2018-10-25T09:21:34.091Z"
                        },
                        {
                            "name": "No intent",
                            "description": "no intent",
                            "createdAt": "2018-10-25T09:21:34.091Z",
                            "modifiedAt": "2018-10-25T09:21:34.091Z"
                        }
                    ],
                    "patterns": [],
                    "phrases": [],
                    "synonyms": []
                }
            }
        ],
        "import2": [
            {
                "datasource": {
                    "serviceid": "09jmqzfmvkU9CmOxR40E40YTp3FGvO5WhQSsZUX9iFJTOXE43AuPlpV81hPHFVz9",
                    "utterances": [
                        {
                            "utterance": "Accident",
                            "case_converted_utterance": "Accident",
                            "mapping": "{\"tokens\": [\"Accident\"], \"intent\": \"HIGH\", \"tags\": []}",
                            "ir_trained": true,
                            "ner_trained": true
                        },
                        {
                            "utterance": "Helloooooo ",
                            "case_converted_utterance": "Helloooooo ",
                            "mapping": "{\"tokens\": [\"Helloooooo\"], \"intent\": \"greetings\", \"tags\": []}",
                            "ir_trained": true,
                            "ner_trained": true
                        },
                        {
                            "utterance": "Hii ",
                            "case_converted_utterance": "Hii ",
                            "mapping": "{\"tokens\": [\"Hii\"], \"intent\": \"hi\", \"tags\": []}",
                            "ir_trained": true,
                            "ner_trained": true
                        },
                        {
                            "utterance": "Hello ",
                            "case_converted_utterance": "Hello ",
                            "mapping": "{\"tokens\": [\"Hello\"], \"intent\": \"greetings\", \"tags\": []}",
                            "ir_trained": true,
                            "ner_trained": true
                        },
                        {
                            "utterance": "Hi ",
                            "case_converted_utterance": "Hi ",
                            "mapping": "{\"tokens\": [\"Hi\"], \"intent\": \"greetings\", \"tags\": []}",
                            "ir_trained": true,
                            "ner_trained": true
                        },
                        {
                            "utterance": "i want to open a account",
                            "case_converted_utterance": "i want to open a account",
                            "mapping": "{\"tokens\": [[\"i\", 0], [\"want\", 2], [\"to\", 7], [\"open\", 10], [\"a\", 15], [\"account\", 17]], \"text\": \"i want to open a account\", \"intent\": \"account\", \"id\": 0, \"tags\": [{\"start\": 3, \"tag\": \"account\", \"end\": 6, \"entity\": \"open a account\"}]}",
                            "ir_trained": true,
                            "ner_trained": true
                        },
                        {
                            "utterance": "i want a 4 year loan",
                            "case_converted_utterance": "i want a 4 year loan",
                            "mapping": "{\"tokens\": [[\"i\", 0], [\"want\", 2], [\"a\", 7], [\"4\", 9], [\"year\", 11], [\"loan\", 16]], \"text\": \"i want a 4 year loan\", \"intent\": \"openaccount\", \"id\": 3, \"tags\": [{\"start\": 3, \"tag\": \"loan\", \"end\": 5, \"entity\": \"4 year\"}]}",
                            "ir_trained": true,
                            "ner_trained": true
                        },
                        {
                            "utterance": "how can i open a account",
                            "case_converted_utterance": "how can i open a account",
                            "mapping": "{\"tokens\": [[\"how\", 0], [\"can\", 4], [\"i\", 8], [\"open\", 10], [\"a\", 15], [\"account\", 17]], \"text\": \"how can i open a account\", \"intent\": \"openaccount\", \"id\": 4, \"tags\": [{\"start\": 3, \"tag\": \"account\", \"end\": 6, \"entity\": \"open a account\"}]}",
                            "ir_trained": true,
                            "ner_trained": true
                        },
                        {
                            "utterance": "i want a savings account",
                            "case_converted_utterance": "i want a savings account",
                            "mapping": "{\"tokens\": [[\"i\", 0], [\"want\", 2], [\"a\", 7], [\"savings\", 9], [\"account\", 17]], \"text\": \"i want a savings account\", \"intent\": \"openaccount\", \"id\": 5, \"tags\": [{\"start\": 3, \"tag\": \"account\", \"end\": 5, \"entity\": \"savings account\"}]}",
                            "ir_trained": true,
                            "ner_trained": true
                        },
                        {
                            "utterance": "i want to have a loan ",
                            "case_converted_utterance": "i want to have a loan ",
                            "mapping": "{\"tokens\": [[\"i\", 0], [\"want\", 2], [\"to\", 7], [\"have\", 10], [\"a\", 15], [\"loan\", 17], [\"\", 22]], \"text\": \"i want to have a loan \", \"intent\": \"openaccount\", \"id\": 6, \"tags\": [{\"start\": 5, \"tag\": \"loan\", \"end\": 6, \"entity\": \"loan\"}]}",
                            "ir_trained": true,
                            "ner_trained": true
                        },
                        {
                            "utterance": "please help me with opening account",
                            "case_converted_utterance": "please help me with opening account",
                            "mapping": "{\"tokens\": [[\"please\", 0], [\"help\", 7], [\"me\", 12], [\"with\", 15], [\"opening\", 20], [\"account\", 28]], \"text\": \"please help me with opening account\", \"intent\": \"openaccount\", \"id\": 7, \"tags\": [{\"start\": 4, \"tag\": \"account\", \"end\": 6, \"entity\": \"opening account\"}]}",
                            "ir_trained": true,
                            "ner_trained": true
                        },
                        {
                            "utterance": "please block my card",
                            "case_converted_utterance": "please block my card",
                            "mapping": "{\"tokens\": [[\"please\", 0], [\"block\", 7], [\"my\", 13], [\"card\", 16]], \"text\": \"please block my card\", \"intent\": \"blocking\", \"id\": 6, \"tags\": [{\"start\": 1, \"tag\": \"card\", \"end\": 4, \"entity\": \"block my card\"}]}",
                            "ir_trained": true,
                            "ner_trained": true
                        },
                        {
                            "utterance": "how can i block my card",
                            "case_converted_utterance": "how can i block my card",
                            "mapping": "{\"tokens\": [[\"how\", 0], [\"can\", 4], [\"i\", 8], [\"block\", 10], [\"my\", 16], [\"card\", 19]], \"text\": \"how can i block my card\", \"intent\": \"blocking\", \"id\": 7, \"tags\": [{\"start\": 3, \"tag\": \"card\", \"end\": 6, \"entity\": \"block my card\"}]}",
                            "ir_trained": true,
                            "ner_trained": true
                        },
                        {
                            "utterance": "block my card please",
                            "case_converted_utterance": "block my card please",
                            "mapping": "{\"tokens\": [[\"block\", 0], [\"my\", 6], [\"card\", 9], [\"please\", 14]], \"text\": \"block my card please\", \"intent\": \"blocking\", \"id\": 8, \"tags\": [{\"start\": 0, \"tag\": \"card\", \"end\": 3, \"entity\": \"block my card\"}]}",
                            "ir_trained": true,
                            "ner_trained": true
                        },
                        {
                            "utterance": "help me to block my card ",
                            "case_converted_utterance": "help me to block my card ",
                            "mapping": "{\"tokens\": [[\"help\", 0], [\"me\", 5], [\"to\", 8], [\"block\", 11], [\"my\", 17], [\"card\", 20], [\"\", 25]], \"text\": \"help me to block my card \", \"intent\": \"blocking\", \"id\": 9, \"tags\": [{\"start\": 3, \"tag\": \"card\", \"end\": 6, \"entity\": \"block my card\"}]}",
                            "ir_trained": true,
                            "ner_trained": true
                        },
                        {
                            "utterance": "please help me to do payment",
                            "case_converted_utterance": "please help me to do payment",
                            "mapping": "{\"tokens\": [[\"please\", 0], [\"help\", 7], [\"me\", 12], [\"to\", 15], [\"do\", 18], [\"payment\", 21]], \"text\": \"please help me to do payment\", \"intent\": \"payment\", \"id\": 10, \"tags\": []}",
                            "ir_trained": true,
                            "ner_trained": true
                        },
                        {
                            "utterance": "how can i do the payment",
                            "case_converted_utterance": "how can i do the payment",
                            "mapping": "{\"tokens\": [[\"how\", 0], [\"can\", 4], [\"i\", 8], [\"do\", 10], [\"the\", 13], [\"payment\", 17]], \"text\": \"how can i do the payment\", \"intent\": \"payment\", \"id\": 11, \"tags\": []}",
                            "ir_trained": true,
                            "ner_trained": true
                        },
                        {
                            "utterance": "i want to do the payment",
                            "case_converted_utterance": "i want to do the payment",
                            "mapping": "{\"tokens\": [[\"i\", 0], [\"want\", 2], [\"to\", 7], [\"do\", 10], [\"the\", 13], [\"payment\", 17]], \"text\": \"i want to do the payment\", \"intent\": \"payment\", \"id\": 12, \"tags\": []}",
                            "ir_trained": true,
                            "ner_trained": true
                        },
                        {
                            "utterance": "please process my payment",
                            "case_converted_utterance": "please process my payment",
                            "mapping": "{\"tokens\": [[\"please\", 0], [\"process\", 7], [\"my\", 15], [\"payment\", 18]], \"text\": \"please process my payment\", \"intent\": \"payment\", \"id\": 13, \"tags\": []}",
                            "ir_trained": true,
                            "ner_trained": true
                        }
                    ],
                    "entities": [
                        "account",
                        "card",
                        "hi",
                        "NAME",
                        "AGER"
                    ],
                    "intents": [
                        {
                            "name": "payment",
                            "description": "payment",
                            "createdAt": "2018-10-25T09:21:34.090Z",
                            "modifiedAt": "2018-10-25T09:21:34.090Z"
                        },
                        {
                            "name": "blocking",
                            "description": "blocking",
                            "createdAt": "2018-10-25T09:21:34.090Z",
                            "modifiedAt": "2018-10-25T09:21:34.090Z"
                        },
                        {
                            "name": "openaccount",
                            "description": "openaccount",
                            "createdAt": "2018-10-25T09:21:34.090Z",
                            "modifiedAt": "2018-10-25T09:21:34.090Z"
                        },
                        {
                            "name": "greetings",
                            "description": "greetings",
                            "createdAt": "2018-10-25T09:21:34.090Z",
                            "modifiedAt": "2018-10-25T09:21:34.090Z"
                        },
                        {
                            "name": "account",
                            "description": "account",
                            "createdAt": "2018-10-25T09:21:34.090Z",
                            "modifiedAt": "2018-10-25T09:21:34.090Z"
                        },
                        {
                            "name": "hiu",
                            "description": "hiu",
                            "createdAt": "2018-10-25T09:21:34.090Z",
                            "modifiedAt": "2018-10-25T09:21:34.090Z"
                        },
                        {
                            "name": "hi",
                            "description": "hi",
                            "createdAt": "2018-10-25T09:21:34.090Z",
                            "modifiedAt": "2018-10-25T09:21:34.090Z"
                        },
                        {
                            "name": "HIGH",
                            "description": "HIGH",
                            "createdAt": "2018-10-25T09:21:34.090Z",
                            "modifiedAt": "2018-10-25T09:21:34.090Z"
                        },
                        {
                            "name": "LOW",
                            "description": "LOW",
                            "createdAt": "2018-10-25T09:21:34.090Z",
                            "modifiedAt": "2018-10-25T09:21:34.090Z"
                        },
                        {
                            "name": "MEDIUM",
                            "description": "MEDIUM",
                            "createdAt": "2018-10-25T09:21:34.090Z",
                            "modifiedAt": "2018-10-25T09:21:34.090Z"
                        },
                        {
                            "name": "details",
                            "description": "details",
                            "createdAt": "2018-10-25T09:21:34.090Z",
                            "modifiedAt": "2018-10-25T09:21:34.090Z"
                        },
                        {
                            "name": "No intent",
                            "description": "no intent",
                            "createdAt": "2018-10-25T09:21:34.090Z",
                            "modifiedAt": "2018-10-25T09:21:34.090Z"
                        }
                    ],
                    "patterns": [],
                    "phrases": [],
                    "synonyms": []
                }
            }
        ],
        "import3": [
            {
                "datasource": {
                    "serviceid": "09lDfVcdeWRNSUZhJwBPNCZ0s3yHZqMhoqcsJ5YPr6sK0wHbD6nhTfcxvrvkCv2w",
                    "utterances": [
                        {
                            "utterance": " FTP Failure host ukprodaps",
                            "case_converted_utterance": " FTP Failure host ukprodaps",
                            "mapping": "{\"tokens\": [[\"\", 0], [\"FTP\", 1], [\"Failure\", 5], [\"host\", 13], [\"ukprodaps\", 18]], \"text\": \" FTP Failure host ukprodaps\", \"intent\": \"Job error\", \"id\": 0, \"tags\": [{\"start\": 4, \"tag\": \"HOST\", \"end\": 5, \"entity\": \"ukprodaps\"}]}",
                            "ir_trained": true,
                            "ner_trained": false
                        },
                        {
                            "utterance": " FTP Failure host kpoodaps",
                            "case_converted_utterance": " FTP Failure host kpoodaps",
                            "mapping": "{\"tokens\": [[\"\", 0], [\"FTP\", 1], [\"Failure\", 5], [\"host\", 13], [\"kpoodaps\", 18]], \"text\": \" FTP Failure host kpoodaps\", \"intent\": \"Job error\", \"id\": 1, \"tags\": [{\"start\": 4, \"tag\": \"HOST\", \"end\": 5, \"entity\": \"kpoodaps\"}]}",
                            "ir_trained": true,
                            "ner_trained": false
                        },
                        {
                            "utterance": "FTP Failure host ppoodaps",
                            "case_converted_utterance": "FTP Failure host ppoodaps",
                            "mapping": "{\"tokens\": [[\"FTP\", 0], [\"Failure\", 4], [\"host\", 12], [\"ppoodaps\", 17]], \"text\": \"FTP Failure host ppoodaps\", \"intent\": \"Job error\", \"id\": 2, \"tags\": [{\"start\": 3, \"tag\": \"HOST\", \"end\": 4, \"entity\": \"ppoodaps\"}]}",
                            "ir_trained": true,
                            "ner_trained": true
                        },
                        {
                            "utterance": "FTP Failure host kpoodapj",
                            "case_converted_utterance": "FTP Failure host kpoodapj",
                            "mapping": "{\"tokens\": [[\"FTP\", 0], [\"Failure\", 4], [\"host\", 12], [\"kpoodapj\", 17]], \"text\": \"FTP Failure host kpoodapj\", \"intent\": \"Job error\", \"id\": 3, \"tags\": [{\"start\": 3, \"tag\": \"HOST\", \"end\": 4, \"entity\": \"kpoodapj\"}]}",
                            "ir_trained": true,
                            "ner_trained": true
                        },
                        {
                            "utterance": "FTP Failure host kpopdaps",
                            "case_converted_utterance": "FTP Failure host kpopdaps",
                            "mapping": "{\"tokens\": [[\"FTP\", 0], [\"Failure\", 4], [\"host\", 12], [\"kpopdaps\", 17]], \"text\": \"FTP Failure host kpopdaps\", \"intent\": \"Job error\", \"id\": 4, \"tags\": [{\"start\": 3, \"tag\": \"HOST\", \"end\": 4, \"entity\": \"kpopdaps\"}]}",
                            "ir_trained": true,
                            "ner_trained": true
                        },
                        {
                            "utterance": "my name is mahesh",
                            "case_converted_utterance": "my name is mahesh",
                            "mapping": "{\"tokens\": [[\"my\", 0], [\"name\", 3], [\"is\", 8], [\"mahesh\", 11]], \"text\": \"my name is mahesh\", \"intent\": \"IdentifyUser\", \"id\": 5, \"tags\": [{\"start\": 3, \"tag\": \"Name\", \"end\": 4, \"entity\": \"mahesh\"}]}",
                            "ir_trained": true,
                            "ner_trained": true
                        },
                        {
                            "utterance": "I am TestUser",
                            "case_converted_utterance": "I am TestUser",
                            "mapping": "{\"tokens\": [[\"I\", 0], [\"am\", 2], [\"TestUser\", 5]], \"text\": \"I am TestUser\", \"intent\": \"IdentifyUser\", \"id\": 6, \"tags\": [{\"start\": 2, \"tag\": \"Name\", \"end\": 3, \"entity\": \"TestUser\"}]}",
                            "ir_trained": true,
                            "ner_trained": true
                        }
                    ],
                    "entities": [
                        "HOST",
                        "Name"
                    ],
                    "intents": [
                        {
                            "name": "Job error",
                            "description": "Job error",
                            "createdAt": "2018-10-25T09:21:34.097Z",
                            "modifiedAt": "2018-10-25T09:21:34.097Z"
                        },
                        {
                            "name": "IdentifyUser",
                            "description": "IdentifyUser",
                            "createdAt": "2018-10-25T09:21:34.097Z",
                            "modifiedAt": "2018-10-25T09:21:34.097Z"
                        },
                        {
                            "name": "No intent",
                            "description": "no intent",
                            "createdAt": "2018-10-25T09:21:34.097Z",
                            "modifiedAt": "2018-10-25T09:21:34.097Z"
                        }
                    ],
                    "patterns": [],
                    "phrases": [],
                    "synonyms": []
                }
            }
        ]
    }
}

#######################################################################################################################
Save Project details:

Query:
const saveProjectConfigQuery = `
    mutation AddProjectConfig($input: addProjectConfigInput!){
      addProjectConfig(input: $input){
        changedProjectConfigEdge{
          node{
            _id
            id
          }
        }
      }
    }
`;

Request URL:
http://ice-xd.southindia.cloudapp.azure.com:3001/project/manage

POST Data:
{"input":{"clientMutationId":"random","project":"5d147a86144b351403308f6a"}}

JSON Response:
{
    "data": {
        "addProjectConfig": {
            "changedProjectConfigEdge": {
                "node": {
                    "_id": "5d147a86144b351403308f6b",
                    "id": "UHJvamVjdENvbmZpZzo1ZDE0N2E4NjE0NGIzNTE0MDMzMDhmNmI="
                }
            }
        }
    }
}

#######################################################################################################################
Update Project Config Details:

Query:
const updateProjectConfigQuery = `
  mutation UpdateProjectConfig($input: updateProjectConfigInput!) {
      updateProjectConfig(input: $input) {
        changedProjectConfig{
          id
          _id
          serviceid
          project{
            id
           _id
           name
          }
          datasource{
            _id
            utterances{
              utterance
              case_converted_utterance
              mapping
              ir_trained
              ner_trained
            }
            intents{
              name
              description
              createdAt
              modifiedAt
            }
            entities
            predefined_entities
            patterns{
              pattern
              entity
            }
            phrases{
              phrase
              entity
            }
            synonyms{
              synonym
              word
            }
            }
          }
        }
      }
    `;


Request URL:
http://ice-xd.southindia.cloudapp.azure.com:3001/project/manage

POST Data:
{
    "input": {
        "id": "5d1486bd144b351403310b51",
        "clientMutationId": "random",
        "datasource": "5d1486bd144b351403310b52",
        "serviceid": "0ApEds1WN5pbN2QNA3PV2lBjBRjTMKr3uitFUqhUwD88VJPXLe9ikEO3eKMydULL"
    }
}

JSON Response:
{
    "data": {
        "updateProjectConfig": {
            "changedProjectConfig": {
                "id": "UHJvamVjdENvbmZpZzo1ZDE0ODZiZDE0NGIzNTE0MDMzMTBiNTE=",
                "_id": "5d1486bd144b351403310b51",
                "serviceid": "0ApEds1WN5pbN2QNA3PV2lBjBRjTMKr3uitFUqhUwD88VJPXLe9ikEO3eKMydULL",
                "project": {
                    "id": "UHJvamVjdDo1ZDE0ODZiYzE0NGIzNTE0MDMzMTBiNTA=",
                    "_id": "5d1486bc144b351403310b50",
                    "name": "wwww"
                },
                "datasource": {
                    "_id": "5d1486bd144b351403310b52",
                    "utterances": [],
                    "intents": [
                        {
                            "name": "No intent",
                            "description": "Add the utterances that should not be labelled as any of your intents here.",
                            "createdAt": "2019-06-27T09:05:01.439Z",
                            "modifiedAt": "2019-06-27T09:05:01.439Z"
                        }
                    ],
                    "entities": [],
                    "predefined_entities": [],
                    "patterns": [],
                    "phrases": [],
                    "synonyms": []
                }
            }
        }
    }
}

#######################################################################################################################
Load Predefined Intents:

Query:
const loadPredefinedIntentsQuery = ` query GetPredefinedIntents($language: String!){
    predefinedintents(language: $language){
      categoryName
      categoryDesc
      language
      intents{
        name
        desc
        utterances
        createdAt
      }
      createdAt
      updatedAt
    }
  }
  `;


Request URL:
http://ice-xd.southindia.cloudapp.azure.com:3001/project/configure/5d1486bc144b351403310b50
5d1486bc144b351403310b50 is the project id.

POST Data:
{"language":"EN"}

JSON Response:
{
    "data": {
        "predefinedintents": [
            {
                "categoryName": "Travel",
                "categoryDesc": "",
                "language": "EN",
                "intents": [
                    {
                        "name": "Booking",
                        "desc": "Indicates that the user wants to make a travel booking",
                        "utterances": [
                            "Flight Ticket",
                            "Book a flight ticket",
                            "I would like to book a flight",
                            "Flight booking",
                            "Book a flight ticket from London to Paris",
                            "Book a travel ticket",
                            "I would like to travel",
                            "Train ticket",
                            "Could you please make a travel booking for me",
                            "Book a cab to travel",
                            "I would like to book a ticket",
                            "Book a train ticket",
                            "Train ticket from Trivandrum to Delhi",
                            "Can you book me a ticket from New York to Boston",
                            "I want to make a travel booking",
                            "Please do a travel booking in London",
                            "Please help in booking a travel ticket",
                            "Travel by bus",
                            "Book a bus ticket from Trivandrum to Cochin",
                            "Book bus ticket"
                        ],
                        "createdAt": "2018-10-03T06:12:54.225Z"
                    },
                    {
                        "name": "Cancellation",
                        "desc": "Indicates that the user wants to cancel a travel booking",
                        "utterances": [
                            "Cancel my ticket",
                            "I want to cancel my travel",
                            "Cancel travel booking",
                            "I do not want to travel anymore , cancel my ticket",
                            "I need to cancel my flight booking",
                            "Cancel my train ticket",
                            "Please cancel my ticket booking",
                            "Cancel my ticket reservation",
                            "I won’t be travelling , cancel",
                            "Cancel booking",
                            "Cancel travel"
                        ],
                        "createdAt": "2018-10-03T06:17:49.378Z"
                    }
                ],
                "createdAt": "2018-10-03T06:12:54.225Z",
                "updatedAt": null
            },
            {
                "categoryName": "HelpDesk",
                "categoryDesc": "",
                "language": "EN",
                "intents": [
                    {
                        "name": "User Account ",
                        "desc": "Indicates that the user has a query regarding his/her account",
                        "utterances": [
                            "I am not able to login",
                            "Forgot my password",
                            "Reset my password",
                            "I am getting login invalid",
                            "I can not access my account",
                            "Change my password to XYZ",
                            "Update my contact details",
                            "My account is deactivated , reactivate it",
                            "I want to activate my account",
                            "Account locked"
                        ],
                        "createdAt": "2018-10-03T07:14:00.468Z"
                    },
                    {
                        "name": "Hardware / Software ",
                        "desc": "Indicates that the user has issues regarding software, hardware configuration, installation etc",
                        "utterances": [
                            "Facing issue with desktop allocation",
                            "Desktop allocation not done for seat Abc01",
                            "I need software upgrade for my system",
                            "Os change request",
                            "Linux operating system installation",
                            "Laptop not issued",
                            "I want to upgrade my RAM",
                            "Issue in installing software",
                            "Internet access in not there in my system",
                            "Need to change the desktop"
                        ],
                        "createdAt": "2018-10-03T07:21:46.384Z"
                    },
                    {
                        "name": "Network ",
                        "desc": "Indicates that the user has network related issues",
                        "utterances": [
                            "My Internet is not working",
                            "Internet access is not there",
                            "Facing connectivity issues",
                            "There is IP conflict for my system",
                            "Need to disable the firewall",
                            "I want to open port 1010 for my system",
                            "Not able to access server Wxyz",
                            "I need a backup to be taken",
                            "Backup required",
                            "Can not access the website www.youtube.com"
                        ],
                        "createdAt": "2018-10-03T07:29:13.235Z"
                    }
                ],
                "createdAt": "2018-10-03T07:14:00.468Z",
                "updatedAt": null
            },
            {
                "categoryName": "Common Medical Symptoms",
                "categoryDesc": "",
                "language": "EN",
                "intents": [
                    {
                        "name": "Feeling dizzy",
                        "desc": null,
                        "utterances": [
                            "i feel dizzy after severe diarrhea",
                            "when i wake up in the morning i feel dizzy",
                            "Every time I make an effort, I felt dizzy.",
                            "When I stand up too quickly I start to feel dizzy and light-headed",
                            "I feel lightheaded",
                            "I feel dizzy when I set in-front of my laptop for an hour or two, what possibly could be the reason?",
                            "My head gets dizzy when I try to get up.",
                            "When I stand I feel dizzy I do not know why",
                            "I feel dizzy whenever I stand up.",
                            "When i'm awake in the morning I feel strange and have vertigo",
                            "I feel dizzy after doing a muscular effort.",
                            "I feel lightheaded when I stand up",
                            "Whenever I stand up I feel dizzy.",
                            "I feel dizzy when i make sudden movements",
                            "When I stand up, I feel like I'm going to fall down instantly",
                            "I feel like the world goes round and round",
                            "I feel like the room is spinning",
                            "When I'm too high I start to feel dizzy",
                            "I'm not good i feel dizzy",
                            "My head is spinning when I get up.",
                            "I feel dizzy and out of sight",
                            "When I stand up too quickly I feel as though I'm going to faint.",
                            "All of a sudden I felt dizzy when I stood up.",
                            "when i get up, i feel dizzy and fall down.",
                            "i was travelling by ship and i feel dizzy.",
                            "When I go to stand, my head starts swirling"
                        ],
                        "createdAt": "2018-09-18T12:51:09.542Z"
                    },
                    {
                        "name": "Acne",
                        "desc": null,
                        "utterances": [
                            "I feel deep Tingling when I touch Acne followed by bad sensation",
                            "My acne gets worse when it is hot",
                            "chronic disease of hair follicles and sebaceous glands.",
                            "I used to have acne when I was 15 years old",
                            "Even though I'm an adult my face keeps breaking out in pimples.",
                            "I break out on my face very frequently",
                            "I hate my acne.",
                            "My face break out badly every month around my cycle.",
                            "I got acne when I ate chili",
                            "My chest break out with red pimples and whiteheads.",
                            "I get breakouts on my chest with red patches that get more intense when i get hot.",
                            "My chest acne breaks out and never clears up.",
                            "Is there a cure for acne?",
                            "there is acne on my face",
                            "I have pimples in patches along with a lot of redness on my face.",
                            "My son has a lot of acne.",
                            "The acne was causing me to feel embarrassed.",
                            "I have eruptions on my face that come and go .",
                            "Chronic disease of hair follicles and sebaceous glands",
                            "Is pimples a skin disease?",
                            "I never had any acne problem until my last pregnancy, when all of a sudden my back got covered in zits.",
                            "My acne itches and oozes.",
                            "I can't get a girlfriend because of my acne.",
                            "I get big patches of irritated pimples on my back and they hurt.",
                            "There are some pimples on my face that bother me a lot",
                            "My acne is really embarassing. It's so read.",
                            "In highschool I had a lot of acne.",
                            "I get clusters of pimples on my face that never go away.",
                            "I have pimples on my back.",
                            "My face is all broken out with pimples.",
                            "Sometimes when it is cold outside, my face hurts, especially around the pimples that are ready to pop.",
                            "My face has broken out in painful red spots and lumps, that no matter how much I clean my face don't seem to be going away.",
                            "I get clusters of whiteheads and blackheads on my back.",
                            "I have acne all over my face"
                        ],
                        "createdAt": "2018-09-18T12:51:09.542Z"
                    },
                    {
                        "name": "Blurry vision",
                        "desc": null,
                        "utterances": [
                            "I have cloudy eyes",
                            "I tried to put my glasses to see more clear but cant find any change",
                            "i can't see well",
                            "i have a problem in seeing objects it is too difficult to see",
                            "I have a blurry vision during my swimming training in the pool, why?",
                            "My television and computer seem out of focus even though I have new glasses.",
                            "I feel pain in my eyes I can see fog",
                            "i can't ride my car at night because i have blurry vision.",
                            "Everything looks like beeing in a smoky area.",
                            "When I stand up too quick my vision is blurry.",
                            "I can't see the sign I have a blurry vision",
                            "When I eat sugar I notice my vision blurs.",
                            "It's hard to see things",
                            "I'm having a hard time reading because the letters are all fuzzy",
                            "I am worried for my driving, because I can barely focus when I am at the wheel, my eyes feel teary.",
                            "When I force my eyes to view I have blurry vision.",
                            "I have a blurry vision since I woke up this morning, what could be the reason?",
                            "Sterilizer for the eye",
                            "i am having problems seeing things feel like a cloud on my eyes everything is blurry",
                            "I have blurred vision.",
                            "I have blurry vision after I used a wrong medicine.",
                            "When i'm driving my eyes see in double",
                            "I have a blurry vision after my head was hit yesterday.",
                            "I noticed an important decrease in my vision when I try to look at things up close.",
                            "i was watching tv and suddenly have blurry vision",
                            "I have a blurry vision and i can't see in the darkness , what is the reason doctor ?"
                        ],
                        "createdAt": "2018-09-18T12:51:09.542Z"
                    },
                    {
                        "name": "Injury from sports",
                        "desc": null,
                        "utterances": [
                            "I have cut my finger because of playing football and I have to apply pain relief cream but it does not help",
                            "i cant sleep because of cold",
                            "My back got injured while i was lifting at the gym",
                            "I stopped sports because I get Injury from sports",
                            "I was playing soccer and I twisted my ankle",
                            "I had a collision while playing soccer.  My knee buckled and now it's unstable.",
                            "i was playing basketball yesterday, i have sprained ankle",
                            "i have injured myself during the soccer match",
                            "When I played football I dislocated my shoulder",
                            "I feel pain in my right shoulder after the tennis match.",
                            "I hit my head at the basketball game.  Could I have a concussion?",
                            "I feel strong pain in my knee after it was hit during the football match.",
                            "i hit the ground when trying to shoot a basketball",
                            "When I was young I had an injury from sports in my knee.",
                            "I broke my ankle while doing rock climbing in the Carpathians.",
                            "I hve cut my finger because of playing football and I  to apply pain relief cream but it does not help",
                            "I got injured exercising",
                            "i was injured during football match, i was diagnosed with Cruciate ligament",
                            "i'm injured i can't play sports",
                            "I feel great pain in my feet after playing one of the sports games",
                            "I may have overdone it with the weightlifting, because I am afraid I may have torn a muscle on my back.",
                            "I was very active in sports but now my body is feeling pain.",
                            "I was kicked in the head playing soccer last night.",
                            "I toppled over while jumping to catch the ball.",
                            "I started taking swimming lessons and I guess I swallowed too much water through my nose, because this sinusitis is killing me now.",
                            "I think I sprained my ankle it really hurts.",
                            "This long scar on my left buttock is from falling off my mountain bike."
                        ],
                        "createdAt": "2018-09-18T12:51:09.542Z"
                    },
                    {
                        "name": "Shoulder pain",
                        "desc": null,
                        "utterances": [
                            "i can't move my shoulder because of pain",
                            "It feels like someone stuck a knife into my shoulder",
                            "I feel pain in my shoulders when I write on the keyboard.",
                            "i have shoulder pain after doing any home work.",
                            "I can't carry anything I have a pain in my shoulder",
                            "When I move my shoulder, it's like lightning is being sent through my shoulder",
                            "i feel that is great pain in my left shoulder",
                            "There is so much pain when I move my arm.",
                            "It hurts when I raise my arm up",
                            "My right shoulder clicks when I move my arm.",
                            "my shoulder is hurting me",
                            "i have a strong shoulder pain",
                            "I can't stand with this horrible feeling in my shoulder",
                            "My shoulder aches when I try to lift five pounds.",
                            "I have shoulder pain when I try to carry my groceries.",
                            "My shoulder hurts me so much",
                            "when i raise my hand i feel pain in my shoulder.",
                            "Why is my shoulder aching when I try to pick up the laundry?",
                            "I have throbing in my shoulder",
                            "I have severe shoulder pain",
                            "My shoulder hurts when I try to reach something above my head.",
                            "Yesterday I had a shouder pain",
                            "My shoulder has agreat pain",
                            "There feels like a swollen knot at my shoulderblade with pain shooting from that",
                            "I feel a great pain in my shoulder when i try to lift something heavy",
                            "I don't have full range of motion with my arms",
                            "When I move on my shoulder, pain shoots down my arm",
                            "I feel shoulder pain at intervals of time.",
                            "I feel like I went to an acupuncture's practice and had 100 needles in my shoulder",
                            "I carried a heavy bag yesterday and when I get up today I felt a great shoulder pain.",
                            "Anytime I play tennis I feel a shoulder pain",
                            "When I lift my arms up I have a soreness in my shoulders"
                        ],
                        "createdAt": "2018-09-18T12:51:09.542Z"
                    },
                    {
                        "name": "Hair falling out",
                        "desc": null,
                        "utterances": [
                            "My hair is falling out in huge amount",
                            "My shower drain is full of hair every time.",
                            "when i was washing my hair it was falling out heavily",
                            "my hair falling out",
                            "When I brush my hair I notice big clumps of hair coming out in the brush.",
                            "A terrible fall in hair",
                            "itch at front and center of scalp",
                            "my hair isn't well",
                            "I'm very worried that I'll go bald soon. Am I very sick?",
                            "I lose a lot of my hair",
                            "There are lots of hairs on my pillow in the morning.",
                            "My hair is coming out in chunks, especially when I wash it",
                            "I'm in need for a treatment for my hair fall",
                            "I have a hair shortage",
                            "My hair always falls out and i have lost a lot of hair lately",
                            "I feel depressed when I see my hair falling out",
                            "I visited many doctors but they can't find the right treatment toget my hair back",
                            "My hair is falling when I am combing it.",
                            "Mr hair is falling out just by combing it.",
                            "I notice a lot more hair coming out than usual when I brush my hair",
                            "I've noticed my hair falling out a lot lately.",
                            "My hair is falling out after I take a shower.",
                            "Every time I comb my hair there are so many hair in my comb.",
                            "My hair is falling out in bunches.",
                            "When I tried to take care if my hair I found that it is falling out",
                            "My hair is falling without a reason, I can see a lot of hair on my working desk.",
                            "using hair tonic"
                        ],
                        "createdAt": "2018-09-18T12:51:09.542Z"
                    },
                    {
                        "name": "Body feels weak",
                        "desc": null,
                        "utterances": [
                            "I can't do anything I feel a weak in my body",
                            "I get tired too fast, I can barely put on my clothes in the morning.",
                            "When I get out of bed in the morning my body feels very weak.",
                            "I have tried to relief it but I can't",
                            "My muscles feel tired",
                            "My body feels weak and I tried to make it relax but it stills pain me",
                            "My body feels weak although I take my vitamins regularly.",
                            "can't do any exercise, i feel weak",
                            "It's hard to stand up, and I'm moving very slowly",
                            "When I eat too much sugar my body gets weak and dizzy.",
                            "I don't do anything at home and still I feel exhausted.",
                            "My body feels weak after my first day in the gym, why?",
                            "I feel discomfort throughout the body in general",
                            "I hardly have enough stength to get up,",
                            "I feel weak all over.",
                            "My body feels weak although I eat a lot, why?",
                            "I don't have the energy to do the things that I used to",
                            "My body feels weak and i think that my face is fade and i can't sleep well",
                            "I have the impression of having no strength in my body",
                            "my cbc report indicate 10 hb, i feel tired of little work.",
                            "Sometimes my body feels week without reason",
                            "i am feeling so dizzy, body is so fragile.",
                            "I feel very weak in my body",
                            "I've always been very active but now I just don't have the strength or energy to go for even a short walk.",
                            "i feel weak"
                        ],
                        "createdAt": "2018-09-18T12:51:09.542Z"
                    },
                    {
                        "name": "Heart hurts",
                        "desc": null,
                        "utterances": [
                            "there is too much pain when i move my arm",
                            "dr. I feel a strange and powerful pain inside my rib cage",
                            "I often get a sharp pain in my chest and I can't tell what I'm doing that might be triggering it.",
                            "My heart is beating fast and it scares me.",
                            "I feel heart pain when I walk a lot",
                            "i have a great pain in my thorax from heart injury",
                            "I feel increased heart rate with prick",
                            "heart aches so much",
                            "It is like I have a needle pushing through my heart.",
                            "I feel a pain on the left side of my chest, where my heart is",
                            "I feel pain in my heart when I wake up",
                            "There is this pain that radiates from my chest up to my left arm.",
                            "My heart hurts while I'm sad, why?",
                            "My husband left me for another woman, my heart hurts so badly to the point I can't eat or sleep.",
                            "Oh my heart hurts me I tried to be calm and I can't",
                            "I feel hurts in my heart",
                            "The crushing sensation on my heart leaves me breathless.",
                            "my heart hurts me",
                            "I felt my heart hurts when I ran for along distance",
                            "My heart feels like it's going to explode.",
                            "I have pain in my chest that saddens me.",
                            "The area around my heart doesn't feel good.",
                            "It feels like my heart is going to leap out of my body. It hurts.",
                            "I have terrible pain in my heart",
                            "I cannot bear this squeezing sensation I have in my chest.",
                            "I cannot breathe because of this dull ache below my left shoulder.",
                            "severe pain in the upper left side of chest and may have pain to back",
                            "I feel a strange and powerful pain inside my rib cage",
                            "My heart hurts when I exercise",
                            "I feel like my heart is on fire."
                        ],
                        "createdAt": "2018-09-18T12:51:09.542Z"
                    },
                    {
                        "name": "Foot ache",
                        "desc": null,
                        "utterances": [
                            "I Have Muscle Pain at my back leg",
                            "I love to walk and be outside but the bottoms of my feet get sore so quickly.",
                            "I can't walk because i have a great foot ache",
                            "My foot is hurting so much.",
                            "The arches of my feet hurt when I wear heels",
                            "I have a foot ache after running 500m with my running shoes.",
                            "I have a foot ache in winter, or when it feels cold, why?",
                            "I have a foot ache although I don't walk a lot.",
                            "i feel pain in my foot",
                            "My foot had been aching since last Tuesday.",
                            "After walking I have some pain under my foot",
                            "My foot hurts and I can't turn it.  Maybe it's broken.",
                            "I knocked my foot and it really hurts.",
                            "i walked a long for 3 km, i feel pain in my foot like foot ache",
                            "The nerves were so damaged during the operation on my ankle that I cannot stand being touched on the scar.",
                            "Had I stepped on a needle it wouldn't have hurt so much, like this damned spur in my heel.",
                            "I can't really jump on my left foot because my triple fracture of the ankle left me with neverending pains.",
                            "I have tried to make massage on my foot but they still pain me",
                            "My foot hurts me a lot of playing football",
                            "there pain in my foot",
                            "I have a painful cramp in my feet",
                            "I can't walk well I have an ache in my foot",
                            "When I walk I get a stabbing pain in the top of my foot",
                            "At first it feels really numb, but then a thousand needles start to prick through my foot.",
                            "i have a great pain in my foot like thrombing pain with relaxing my pain releif",
                            "After an hard working day I have foot ache"
                        ],
                        "createdAt": "2018-09-18T12:51:09.542Z"
                    },
                    {
                        "name": "Feeling cold",
                        "desc": null,
                        "utterances": [
                            "I was diagnosed with  B12-deficiency anemia, which explains why I always felt cold.",
                            "I m feeling cold though the temperature is high",
                            "When I tried to be warm and wear more clothes I found that I was still cold",
                            "When I wake up I am feeling cold",
                            "I'm not good i'm feeling so cold",
                            "There must be something wrong with my blood circulation, I have to wear socks even on the hottest days, my toes are frozen!",
                            "I wake up at night feeling cold",
                            "When I go to sleep I am feeling cold",
                            "I feel cold although we are in summer.",
                            "I am having running nose",
                            "I feel cold and chills even though my clothes are heavy",
                            "I just can't seem to get warm.  Even when everyone around me is warm I always feel cold.",
                            "I couldn't stop shaking or unclench my jaw, that's how cold I was.",
                            "I am always cold, even when I am wearing layers",
                            "I am worried how cold intolerant I am, I am always shivering, even out in the sun.",
                            "I get chills and aches all over.",
                            "i feel cold",
                            "My body feels like it's in a refrigerator.",
                            "I cannot get warm no matter how much I wrap up or how high I put the heating on",
                            "The warming system of my house is broken and  feel so cold",
                            "Even if the temperature is high in the house,  my body is always cold",
                            "I think my body temperature is very low.",
                            "I do not know why I feel cold",
                            "My entire body is freezing.",
                            "my temperature dropped and my body get synosed",
                            "I feel cold when the night comes",
                            "I feel chilly, like an ice cube.  My sister said that she needs several blankets to cover her so that she is warm enough."
                        ],
                        "createdAt": "2018-09-18T12:51:09.542Z"
                    },
                    {
                        "name": "Back pain",
                        "desc": null,
                        "utterances": [
                            "I feel a pain in my back",
                            "My back hurts me and i can't bend it or walk",
                            "I have a back pain since I turned 70 years old.",
                            "i have a problem in my back i cannot extend it",
                            "I feel pain in the lower back",
                            "I have a back pain since I fell on the floor.",
                            "My back is hurting so much.",
                            "When I play sports  I have some burning sensation in my spine",
                            "My back hurts a lot when I bend",
                            "my back hurts me a lot",
                            "When I carry heavy things i feel like breaking my back",
                            "standing less than five minutes and my back start to ache",
                            "i feel pain in my back",
                            "When I bend over I get a shooting pain down my back",
                            "I think I overdid it when I carried all that lumber from the yard. My lower back is killing me.",
                            "I used alot of pain killer to get better but i still feel the same back pain",
                            "longitudinal burning line across back with hard respiratory movements",
                            "My upper back has been sore for a week.",
                            "I feel a pain in my back when I sit on a chair for long.",
                            "I feel pain in my back",
                            "The pain in my back dwwls like a sharp knife in it",
                            "I have a dull ache in  my lower back which makes it difficult to move",
                            "I feel back pain when I carry heavy things",
                            "I have shooting pains up and down my back.",
                            "I love to garden but I get a terrible twinge in my lower back when I lean over.",
                            "I can't stand up or sit down I have a pain in my back that annoys me",
                            "My back hurts so much I can't bend down to tie my shoelaces."
                        ],
                        "createdAt": "2018-09-18T12:51:09.542Z"
                    },
                    {
                        "name": "Internal pain",
                        "desc": null,
                        "utterances": [
                            "I feel a sharp pain in my stomach",
                            "I have a pain internal",
                            "i have pain but i can't specify place",
                            "My body aches on the inside between my hips and shoulders.",
                            "I feel aching on my insides.",
                            "I feel pain inside and I can not identify it",
                            "i feel pain in my body",
                            "My chest hurts when I smoke",
                            "Chronic bowel Pain",
                            "I have constant stomach pain and bloating.",
                            "I have a pain that radiates up from my right hip to my rib cage.  It is at it's worst when I urinate.",
                            "I have internal pain whenever I come down with a cold.",
                            "Sharp pain and heavy breathing",
                            "I feel pain inside I do not know what it is",
                            "I always feel like I have menstrual pains even if I don't have my period.",
                            "There is an extreme pressure below my belly button at the right, which I feel every time I go out for a jog.",
                            "I had internal pain and gases when I ate indian spicy food yesterday",
                            "discomfort or pain that is felt at some point along the front of the body between the neck and upper abdomen.",
                            "I have a head pain every single day.",
                            "I have a pain in my stomach",
                            "What's the symptoms of appendicitis?",
                            "I have general discomfort in my torso.",
                            "I have a dull ache in my stomach.  It gets worse after I eat.",
                            "I have an internal pain I cannot describe",
                            "my left side aches much",
                            "I have a sharp pain in my abdomen."
                        ],
                        "createdAt": "2018-09-18T12:51:09.542Z"
                    },
                    {
                        "name": "Cough",
                        "desc": null,
                        "utterances": [
                            "I have a cold and it makes me cough alot",
                            "I have a dry throat",
                            "Every time I take a deep breath I start coughing",
                            "my child has cough all night, she can't sleep",
                            "I have a lot of mucus when I cough.",
                            "I feel fluid trying to come up when I cough.",
                            "I'm suffering from sharp cough Accompanied by  phlegm",
                            "I usually have a bad cough when I get flu.",
                            "i cant sleep because of cough",
                            "Have severe cold and cough",
                            "I can`t stop coughing.",
                            "There is a constant tickle in my throat",
                            "I cough a lot when I smell perfume, what is wrong with my lungs?",
                            "i have a very bad cough",
                            "My cough is very heavy and I have mucus.",
                            "I can't sleep I have a hard cough",
                            "i have severe dry cough",
                            "i can't breath because of  Cough",
                            "I've had this cough for two weeks.",
                            "My lungs feel heavy like they are filled with mucus",
                            "I can't stop coughing",
                            "I feel like I can hardly breathe unless I get what's in my lungs out",
                            "I feel like I've always got something in my throat",
                            "Sometimes I cough because I'm a smoker",
                            "I have some terrible problems when i'm breathing during the night.",
                            "I've been over my cold for weeks but still cough every day.",
                            "i cant breathe",
                            "I feel pain in my throat",
                            "i have whooping cough with excess mucous, need mucolytic.",
                            "The feeling of coughing increases in winter's reach",
                            "I feel congestion in my chest"
                        ],
                        "createdAt": "2018-09-18T12:51:09.542Z"
                    },
                    {
                        "name": "Skin issue",
                        "desc": null,
                        "utterances": [
                            "I have acne in my face and other problems in my derma like itching",
                            "My infected wound cause fever",
                            "I have dark spots on my skin",
                            "My skin is very dry and peeling.",
                            "I tried alot of cream but i still feel the same skin problem",
                            "My skin is itchy and inflamed",
                            "I have this strange rash on my arm.",
                            "there is a red stain in my skin",
                            "My skin color on my back is red, I don't know why.",
                            "I have found some issues in my skin and tried to use cream but it doesn't get better",
                            "I have a red rash that is itchy on my skin",
                            "I have a rash and it itches very bad.",
                            "I have a scab on the back of my hand that just won't go away.",
                            "I have a very rash sensation close to my arms",
                            "I have a rash on my skin",
                            "Need to scratch my skin every minute",
                            "I have a dry skin",
                            "Something dark is there on my arm",
                            "i have issue with my skin",
                            "red flushes accompanied with itchy",
                            "I feel severe itching in the skin with redness",
                            "I complain alot with skin allergy",
                            "I feel like l fell in hot water",
                            "Every time it rains I get hives on my belly and sides.",
                            "My skin is itching.",
                            "I have acne in my face and other problema in my derma like itching",
                            "When i get up i see my skin vague",
                            "These red spots on my cheeks are new. What is it?",
                            "I have a skin rash after eating an ice-cream."
                        ],
                        "createdAt": "2018-09-18T12:51:09.542Z"
                    },
                    {
                        "name": "Stomach ache",
                        "desc": null,
                        "utterances": [
                            "I have a sharp pain in my lower stomach.",
                            "i have a hard pain in my stomach",
                            "i feel pain in my stomach",
                            "I often get a stomach ache after I eat.  I haven't been able to pinpoint which foods might be the trigger.",
                            "I feel so sore in my stomach area.",
                            "I have an indigestion",
                            "I can't stand with this horrible feeling in my stomach",
                            "The severe pain in the stomach I feel",
                            "My stomach feels starts hurting but then it feels better after I eat something mild.",
                            "I feel abdominal pain",
                            "I have pain in my stomach",
                            "Stomach pain after drinking milk",
                            "I have pain in my colon and my stomach like something cutting it",
                            "I feel a sharp pain in the stomach after eating",
                            "My stomach has been sore since yesterday.",
                            "When i eat i feel my stomach hurts",
                            "My stomach feels full and upset  and bloating after big meals.",
                            "I'm feeling nauseous",
                            "My stomach aches when I eat hot food, why?",
                            "After eating  I have burning sensation inside of me.",
                            "My stomach aches after I drink any soda drink, why?",
                            "I had a sharp pain in my stomach",
                            "I have a great stomach ache and i can't eat any thing",
                            "I feel a burning sensation in my guts about 2 hours after each meal.",
                            "I made lots and lots of analysis to know the main reason for my stomach ache",
                            "cramps along the whole abdomen",
                            "When get up I found that I have a stomach ache  and I tried to take medecine but my stomach still hurting me"
                        ],
                        "createdAt": "2018-09-18T12:51:09.542Z"
                    },
                    {
                        "name": "Hard to breath",
                        "desc": null,
                        "utterances": [
                            "I used to be out of breath after going up a dozen of stairs, but now I struggle to breath even when I sit down.",
                            "i feel that it's hard to breath for me specially after running or making any effort",
                            "Sometimes I feel like a claw on my chest that leaves me breathless.",
                            "I have a problem in the expiration because i have abronchial asthma",
                            "I'm not feeling good I can't take my breath",
                            "I feel a tightness in my chest",
                            "I feel great pressure in my chest",
                            "It is hard to breath when I am in the underground metro station, why?",
                            "I feel like something is squeezing my lungs.",
                            "i was diagnosed with pneumonia, i can't breath easily.",
                            "There are times when I feel crushed under a huge weight and no air passing to my lungs, it actually scares the hell out of me when it happens.",
                            "My heart is pumping fast and I'm having a hard time to breath.",
                            "My chest hurts when I go to take a breath",
                            "My grandmother last year went to hospital because she was having a hard time breathing",
                            "I don't have problems taking in breath but out breath is so heavy",
                            "i can hardly breathe",
                            "It feels like I can't take a deep breath",
                            "I've got a hard time to breath- am I having a heart attack?",
                            "When I walk it's hard to breath.",
                            "I walk every day but now I get short of breath after going only a short way.",
                            "I have difficulty in breathing in crowded places.",
                            "I feel very hard to breathe",
                            "In the morning my respiration is loud.",
                            "I feel something hurt me in taking breath and I cant take my breath",
                            "My nose is congested all the time and there's this gluey secretion in my throat that makes it impossible for me to sleep. I often have to nap sitting down."
                        ],
                        "createdAt": "2018-09-18T12:51:09.542Z"
                    },
                    {
                        "name": "Neck pain",
                        "desc": null,
                        "utterances": [
                            "I have a sharp pain in my neck",
                            "I have a powerful pain inside my neck",
                            "i can't rotate my neck",
                            "I feel a pain in my neck",
                            "i feel pain in my neck",
                            "My throught is so sore.",
                            "I feel pain in my neck after waking up",
                            "My neck has been sore since the accident.",
                            "My neck feels stiff",
                            "my neck hurts me and i can't look down or up",
                            "I can't turn my neck to the left without feeling a stabbing pain",
                            "There's swelling in my neck and it hurts.",
                            "I can't move my head up and down.",
                            "I feel pain in my neck while I'm working.",
                            "I wake up with a stiff neck every morning.  Massage helps but then a couple of days later it's back again.",
                            "Every time I look to left I feel a sharp pain in my neck.",
                            "I have a neck pain when I sit in-front of my laptop.",
                            "Pain in the large neck",
                            "I complain alot with my neck pain and i really need to be better",
                            "I can hardly move my neck.  It hurts.",
                            "There is a tingling sensation in my neck.",
                            "stiffness inability to look right or left except by moving the whole body",
                            "My neck is annoying me I can't sleep bacause of it",
                            "i have difficulty moving my neck",
                            "My neck hurts me and i can't stand with this pain"
                        ],
                        "createdAt": "2018-09-18T12:51:09.542Z"
                    },
                    {
                        "name": "Infected wound",
                        "desc": null,
                        "utterances": [
                            "My son had his lip pierced and it is swollen and the skin inside on his lip is grey and looks infected.",
                            "My muscles in my lower back are aching",
                            "I think my wound is infected",
                            "I cut my hand a couple of weeks ago and even though I keep using an antibiotic cream it's not getting better.",
                            "My son nicked his neck with an old razor and that spot has become inflamed and looks like it is infected.",
                            "surgical wounds red, firing pus, painful and hot to the touch",
                            "My son squeezed a pimple and it broke open only to scab over and now looks like it is infected.",
                            "My grandson cut his foot on a seashell in the ocean and now the foot is turning gray and is puffy.",
                            "My son had a root canal and the dentist accidentally cut the inside of his cheek and now it will not heal.",
                            "My daughter had her eyebrows threaded and it pulled an opening of skin in one of her brows that is now puffy and oozing.",
                            "my hand open wound got infected",
                            "I suffered a deep wound in my hand and I can not stop the bleeding",
                            "There is an injured person",
                            "My daughter was bit by her cat and now her hand is sore, red and swollen and the wound is oozing liquid.",
                            "My daughter had her ears pierced and one of her ear lobes is bright red and burning hot.",
                            "I had a cut that was stitched together but it is not healing.  It is oozing green puss and burns.",
                            "I have a break in the skin inside one of my nostrils that has become infected and is now filled with pus.",
                            "My wound was infected when i was planting some flowers in my garden",
                            "I have a cut on my foot that became infected from using the showers at the gym.",
                            "His infected wound was beginning to rot.",
                            "I'm not feeling good I get infection wound",
                            "The last time I clipped my toenails, I cut them too short and now I have an infected nail.",
                            "I have a cut that has become red and oozes puss.",
                            "My husband has a spot on his lip that he though was cold sore but now it has broken open and leaks fluid all day.",
                            "My cut yellow or greenish-colored pus",
                            "I think there's something wrong with my wound, it does not seem to heal like it should.",
                            "My son got a tattoo several weeks ago and the skin around it is raised and hot and it looks infected.",
                            "My infected wound caused a fever",
                            "I have a cut that is red and swollen.",
                            "My kee is swallowing which indicates i have an infected wound",
                            "My sore looks like its not healing well.",
                            "is my cut infected or just healing?",
                            "You won't believe me, but this infected wound on my hand is from a paper cut I didn't take seriously.",
                            "Surgical wound infections"
                        ],
                        "createdAt": "2018-09-18T12:51:09.542Z"
                    },
                    {
                        "name": "Knee pain",
                        "desc": null,
                        "utterances": [
                            "i have a knee pain when i walk a lot",
                            "i feel pain in my knee",
                            "My knee hurts when I play squash",
                            "My knee catches and hurts when I first stand up after sitting.",
                            "My knee hurts when I walk",
                            "I am struggling to bear weight on my knee, when i stand straight I feel and hear a loud popping noise.",
                            "How do you know if you have a torn meniscus in your knee?",
                            "i can't walk, my knee hurts me",
                            "I feel pain in the knee when walking",
                            "The pain is intense especially when I go down the stairs, it feels like something has snapped inside my knee.",
                            "I could not exercise because of my knee pain",
                            "Chronic bone disease at the level of the doubles of the lower Estremidades",
                            "My knees hurt so bad to walk that I stay sitting more than I should.",
                            "My kneecap feels like it is grating bone on bone when I walk.",
                            "Annoyance starts suddenly, often after an injury or exercise.",
                            "I feel pain in the knee",
                            "My knee doesn't want to bend well.",
                            "My knees seem to grind as I go up or down stairs.",
                            "I fell off my bike and since then I had hard  knee pain",
                            "I feel like there is something swollen and inflamed at the back of my knee.",
                            "I have shooting pain in my kneecap after working out.",
                            "I had a pain in my knee when I was swimming",
                            "The knee feels like it rusted and I suddenly cannot bend it anymore.",
                            "having difficulty moving my knee",
                            "I have a lot of knee pain whenever I go running.",
                            "I can't work good I have a pain in my knee",
                            "My knees ache on cold and rainy days.",
                            "My knee feels weak and it gave way the other day at the top of the stairs.  Luckily there was a rail to hold on to.",
                            "When I walk up a flight of stairs, my right knee hurts.",
                            "I get a knee pain when I walk a lot",
                            "My knees swell right below the knee cap and hurt when I put weight on them.",
                            "redness, swelling, and difficulty walking"
                        ],
                        "createdAt": "2018-09-18T12:51:09.542Z"
                    },
                    {
                        "name": "Head ache",
                        "desc": null,
                        "utterances": [
                            "I read a book for along time and when I finished reading I feel head ache",
                            "My head hurts whenever I try to do something.",
                            "I have front head pain and when I get it the light bothers me.",
                            "I have a dull ache in my head",
                            "my head hurts me badly",
                            "The worst headache was during a hangover in my twenties: I sincerely thought I was going to die from brain inflammation.",
                            "Can't keep focus",
                            "fell skull is cracked like nuts",
                            "I feel a great amount of pressure of my head.",
                            "My head hurts in the back and the pain lasts all day.",
                            "I have a headache almost every day",
                            "My head is so heavy can't think normally",
                            "It feels like someone is hitting my head with a hammer.  I feel pain on the top of my head and it throbs.",
                            "My head hurts when I'm doing this.",
                            "I get terrible headaches every few months and when I get them my vision is affected.",
                            "I have a headache every time I eat ice cream",
                            "My head ache since I woke up this morning.",
                            "I feel a sharp pain in my head when I think too hard.",
                            "My head hurts and I lose the sensation in my face, then lose sight in my eye",
                            "I feel pain in my head with a vertigo",
                            "I have a pain in my head",
                            "When I drink a lot, I get a headache",
                            "I can't stand up, I feel my brain is moving inside my skull.",
                            "I feel great pain in the head",
                            "i feel head ache",
                            "i have a migrain and i took panadol but it doesn√ït help",
                            "When I'm tired I feel my head heavy"
                        ],
                        "createdAt": "2018-09-18T12:51:09.542Z"
                    },
                    {
                        "name": "Open wound",
                        "desc": null,
                        "utterances": [
                            "Laceration, rupture or opening in the skin",
                            "I cut my foot at the pool and it breaks open every day when I walk on it.",
                            "glass broken and wound my leg badly the wound is so wide",
                            "laceration, rupture or opening in the skin",
                            "I have a break in the skin between my thumb and index finger and it will not close.",
                            "I have an open wound in my arm",
                            "I chopped off the tip of my finger while I was cutting some cardboard and I cannot stop the bleeding.",
                            "What helps cuts heal faster?",
                            "My sore isn't healing well and it's been like this for two weeks.",
                            "I hit myself and the would doesn't want to heal",
                            "I cut my finger opening a can, it won't stop bleeding and the wound is gaping and open",
                            "I have a split on my thumb that will not heal.",
                            "The wound is still open",
                            "My wound opened up again",
                            "I cut my hand a couple of days ago and although I didn't think I needed it stitches it hasn't closed up.",
                            "He was discovered to have an open wound.",
                            "I sliced myself deeply with a knife while I was cooking",
                            "I fell through a window while I was cleaning it and I have a shard of glass stuck in my left eye, I think it is pretty serious, please help!",
                            "I have a wound between my toes that gets better overnight and then reopens ever day when I wear dress shoes to work.",
                            "I must see a doctor i have an open wound",
                            "I cut myself and I'm bleeding.",
                            "I had an accident and my wound was open when I arrived to hospital"
                        ],
                        "createdAt": "2018-09-18T12:51:09.542Z"
                    },
                    {
                        "name": "Joint pain",
                        "desc": null,
                        "utterances": [
                            "my ankle is hurting me",
                            "I have a feeling like my whole body is complaining",
                            "I feel pain in my knee when I climb the stairs.",
                            "Feel like something is being jabbed into my joints",
                            "I feel joint pain every time I move",
                            "when i extend my leg there is pain in knee joint",
                            "i have pain like needles in my joints.",
                            "My joints feel swollen",
                            "I feel pain in my joint after an injury in the last football match I played.",
                            "My knee is hurting so badly.",
                            "i can't move my leg, there is pain in the joint",
                            "I feel a sharp pain in my ankle joint when I stand.",
                            "I have some pain when i'm walking around my knees",
                            "I feel a lot of pain in the joints.",
                            "i was playing football and injuried with joint pain.",
                            "I have a sharp pain and clicking sound in my ankle joint when I try to stand on it and walk.",
                            "Feels like there are pins and needles sticking in my joints",
                            "I feel a great pain in my shoulder joint and it does not go away",
                            "When I play football I have joint pain.",
                            "It hurts when I bent my arm",
                            "I fell a stiffness in my elbows and shoulders",
                            "There is pain in my joints. I can not bear pain",
                            "I feel a soreness in my knees when I walk",
                            "I get i joint pain when i try to bend my leg or my arm",
                            "My ankle joint throbs when I put pressure on my foot.",
                            "i have a pain in my elbow joint",
                            "All my body is in a bad case and i need a good treatment",
                            "My joints ache whenever it is cold",
                            "I feel a bone-on-bone pain in my knees when I climb stairs.",
                            "The joints in my fingers are painful in the morning.",
                            "I have a throbbing in my joints",
                            "I have a pain in my joint",
                            "I feel a clicking sensation in my knee each time I step."
                        ],
                        "createdAt": "2018-09-18T12:51:09.542Z"
                    },
                    {
                        "name": "Muscle pain",
                        "desc": null,
                        "utterances": [
                            "my abdominal muscles have great pain since i was at GYM",
                            "There is pain in the muscles I do not know caused",
                            "I feel a burning sensation in my shoulder muscle.",
                            "My muscles in my lower back are aching.",
                            "My shoulder muscle hurts when I try to reach up.",
                            "I need a kind of cream wich make my muscles more relaxed",
                            "The pain feels like it's right below the skin",
                            "There is a sharp pain in my bicep. I have tried to apply pain relief cream but it does not help.",
                            "I have a hard muscle pain since i went to the gym",
                            "My lower back hurts but it improves if I stretch it",
                            "I have a pain in my muscle",
                            "When I wake up in the morning I feel a soreness in my body",
                            "When i'm doing sport I have pain under my skin",
                            "i have a pain in my trapes",
                            "Every morning when I wake up my neck feels like I slept on in wrong.",
                            "My biceps started aching after I went to the gym",
                            "When I play football I have muscle pain.",
                            "There is a sharp pain in my calve.",
                            "My arm hurts when I stretch",
                            "My calves feel like they are tight as knots and are throbbing",
                            "i have muscle pain at my left leg.",
                            "after playing football, i have muscle pain with my both legs.",
                            "When I do hard exercises I feel great pain in my muscles.",
                            "There is a sharp pain in my bicep",
                            "I feel pain in my legs muscles after I ran yesterday, I took some pain killers but it doesn't help.",
                            "I do not feel better in my muscles",
                            "I had alot of exercise yesterday so i feel sharp muscle pains",
                            "I feel muscle pain every time I make an extra effort.",
                            "My muscle in my shoulder burns when I move my arm."
                        ],
                        "createdAt": "2018-09-18T12:51:09.542Z"
                    },
                    {
                        "name": "Ear ache",
                        "desc": null,
                        "utterances": [
                            "I'm not hearing well I have problem with my ear",
                            "I have an ear ache that won't go away.  I don't have a cold or headache or any other symptoms.  Just an earache.",
                            "My left ear is ok, but the right one feels like it's being stabbed with a nail.",
                            "i have a problem in my middle ear made by infection",
                            "I get an ear ache when it is cold",
                            "my ear hurts me badly",
                            "The pain in my ear is unbearable.",
                            "Severe pain in the ear",
                            "My ear hurts and it's worse when I swallow.  My ear is very painful and Tylenol hasn't helped.",
                            "Since I went into the forest  I have pain on my ear",
                            "My ear is ringing.",
                            "I feel pain in my ears with tinnitus",
                            "I think there's fluid in my ears.",
                            "I travelled by plane a few days ago and this time during landing my ears remained clogged and painful.",
                            "I have a sharp pain in my ear",
                            "I'm having a hard time hearing.",
                            "I can't hear out of my ear properly, I feel like there is something in it causing irritation.",
                            "My ear ache when I'm listening to music.",
                            "When I tried to answer the phine call I found that I can't hear the voice of the speaker",
                            "I have an ear ache when showering",
                            "It started as a tinnitus, but today the pain is throbbing and unbearable.",
                            "There is a sharp pain in my ear whenever I do this.",
                            "I had a cold the last time I travelled by plane and I still have a discomfort in my ears.",
                            "It itches inside my ears.",
                            "Hearing any loud sounds makes my ear aches",
                            "My ear hurts when I touch it.",
                            "I have a ear ache when I go to the pool",
                            "When I sneeze very hard I feel ear ache"
                        ],
                        "createdAt": "2018-09-18T12:51:09.542Z"
                    },
                    {
                        "name": "Emotional pain",
                        "desc": null,
                        "utterances": [
                            "When I remember her I feel down",
                            "I feel a huge emotional pain after I broke up with my girlfriend.",
                            "i feel hurt, lot of pain in my heart",
                            "I don't know why I'm constantly sad.",
                            "i'm disappointed",
                            "I feel pain when parting loved ones",
                            "I got a divorce last year and I just can't stop dwelling on how to get revenge on my ex husband.",
                            "I feel suicidal.",
                            "I feel sad like hurt or pain",
                            "I have a mental suffering",
                            "I've tried reading books, but nothing can cheer me up.",
                            "After a breakup  I feel something strange in me.",
                            "I've been feeling very sad lately",
                            "i feel sad",
                            "I wish this excruciating feeling of loss could go away.",
                            "When my grand father died I felt a hard emotional pain",
                            "My mind feels very sad, as if it hurts.  The way I feel in my head is awful and when I think about my break-up, I cry with sadness.",
                            "I feel emotionally crushed",
                            "When I think of my parents I feel pain",
                            "heavy breath with fatigue",
                            "I feel pain when i think of her",
                            "I feel really sad all the time.",
                            "I feel like I just can't cope anymore, I feel overwhelmed and like I just can't get a break.",
                            "i have disterbance in my emotion"
                        ],
                        "createdAt": "2018-09-18T12:51:09.542Z"
                    }
                ],
                "createdAt": "2018-09-18T12:51:09.542Z",
                "updatedAt": null
            },
            {
                "categoryName": "General",
                "categoryDesc": "General category contains the most common intents which are generally used",
                "language": "EN",
                "intents": [
                    {
                        "name": "Greeting",
                        "desc": "Marks the beginning of a conversation",
                        "utterances": [
                            "Good to see you",
                            "Greetings",
                            "Have you been well ?",
                            "Hello agent",
                            "Hello",
                            "Hello I am looking for some help here",
                            "Hey how are you doing",
                            "Hey there all",
                            "Hey there",
                            "Hey twin",
                            "Hey you",
                            "Hi advisor",
                            "Hi there",
                            "How are things going ?",
                            "How are you today ?",
                            "How have you been ?",
                            "How is it going ?",
                            "How R U ?",
                            "Looking good eve",
                            "Ok take me back",
                            "What'S new ?",
                            "What'S up ?",
                            "Who is this ?",
                            "You there",
                            "Good evening",
                            "Good day",
                            "Good morning",
                            "Hi",
                            "Hey",
                            "Hai"
                        ],
                        "createdAt": "2018-08-09T11:15:11.082Z"
                    },
                    {
                        "name": "Conclusion",
                        "desc": "The user wants to end the conversation in a neutral or positive tone",
                        "utterances": [
                            "Bye bye",
                            "See you later",
                            "Ok goodbye",
                            "I'M leaving now",
                            "Im good Thank you",
                            "Im done",
                            "I'M done",
                            "I have got to go",
                            "I am out of here",
                            "I am leaving",
                            "Have a nice day ?",
                            "Good . bye .",
                            "Goodbye",
                            "Going now",
                            "Finished now , good bye",
                            "End trial",
                            "Ending this session",
                            "Cya later",
                            "Catch you later",
                            "Bye now",
                            "See you",
                            "Time to go",
                            "That'S everything",
                            "That is all",
                            "Thank you for your time",
                            "Thanks very much , Bye!",
                            "Thanks , Bye!",
                            "Ok bye"
                        ],
                        "createdAt": "2018-08-09T11:15:11.082Z"
                    },
                    {
                        "name": "Positive Feedback",
                        "desc": "Indicates that the user is happy with the experience",
                        "utterances": [
                            "You'Ve been so helpful : )",
                            "You'Re a Genius!",
                            "You gave me exactly what I Need!",
                            "You are wonderful",
                            "You are the best",
                            "You are great",
                            "You are awesome",
                            "This is so cool",
                            "This is great",
                            "This is good",
                            "Thank you",
                            "Love your work",
                            "I'M looking forward to working with you Again! : )",
                            "I like what you did There! : )",
                            "How cool is this ?",
                            "Can'T believe you are that good",
                            "Brilliant!",
                            "You the man"
                        ],
                        "createdAt": "2018-08-09T11:15:11.082Z"
                    },
                    {
                        "name": "Negative Feedback",
                        "desc": "Indicates that the user is not happy with the experience",
                        "utterances": [
                            "You'Re really frustrating",
                            "You do not seem smart",
                            "You are very frustrating",
                            "You are on my nerves",
                            "You are having delusions",
                            "Why are you stupid ?",
                            "Why are you so annoying ?",
                            "Stupid",
                            "Robots are stupid",
                            "Robots are boring",
                            "Quit annoying me",
                            "It is annoying",
                            "I hate you",
                            "I hate this !",
                            "I do not like you",
                            "Hate you",
                            "Everyone hates you",
                            "Do not like you ?",
                            "You'Re too stupid",
                            "You'Re really irritating",
                            "Shut up",
                            "I quit",
                            "I'D like to stop doing this",
                            "Hey bot go away",
                            "Stop talking to me",
                            "Stop doing this",
                            "Go away",
                            "Go off",
                            "Get lost"
                        ],
                        "createdAt": "2018-08-09T11:15:11.082Z"
                    },
                    {
                        "name": "Switch to Agent",
                        "desc": "Indicates that the user wants to connect to a human agent",
                        "utterances": [
                            "Agent please",
                            "Can I talk to someone real ?",
                            "Connect to a real person",
                            "Speak to a real person",
                            "I want to talk to a human",
                            "A human please",
                            "Can I talk to someone ?",
                            "Is there somebody I can talk to ?",
                            "Can I speak to an agent",
                            "Please connect to a real advisor",
                            "Can I talk to someone with brains ?",
                            "Can you connect me to a real person ?",
                            "Please get me someone who breathes",
                            "Please connect to someone alive"
                        ],
                        "createdAt": "2018-08-09T11:15:11.082Z"
                    },
                    {
                        "name": "Positive Response",
                        "desc": "Indicates that the user wants to continue with the suggested option.",
                        "utterances": [
                            "Sure",
                            "Ok fine",
                            "Please go ahead",
                            "Yes please",
                            "Of course",
                            "Alright I am confirming",
                            "Confirmed",
                            "Okay please proceed",
                            "Okay",
                            "That will be fine",
                            "Ok thanks",
                            "Yes agreed",
                            "Yep",
                            "Yeah",
                            "That works fine"
                        ],
                        "createdAt": "2018-08-09T11:15:11.082Z"
                    },
                    {
                        "name": "Negative Response",
                        "desc": "Indicates that the user does not want to proceed with the option suggested",
                        "utterances": [
                            "No",
                            "Nope",
                            "Dont do that",
                            "Don'T proceed",
                            "Cancel it please",
                            "Not now",
                            "Not that",
                            "Never mind",
                            "No thank you",
                            "Do you have anything better",
                            "Anything else",
                            "Any other option",
                            "No thanks",
                            "That will not work for me"
                        ],
                        "createdAt": "2018-08-09T11:15:11.083Z"
                    },
                    {
                        "name": "Weather",
                        "desc": "Indicates that the user wants to know about the weather",
                        "utterances": [
                            "Cochin weather",
                            "What is the whether now for",
                            "Weather forcast",
                            "Whats weather",
                            "Weather of a place",
                            "Weather of London",
                            "Show me weather",
                            "Weather of La",
                            "Show me weather of Chennai",
                            "Weather of Trivandrum",
                            "Climate of Trivandrum",
                            "Trivandrum weather",
                            "Temperature of Trivandrum",
                            "Temperature of Manchester",
                            "Weather of 23294",
                            "Temperature of 695024",
                            "23394 weather",
                            "99900 weather",
                            "Weather of XXXX XXX"
                        ],
                        "createdAt": "2018-10-03T06:58:26.790Z"
                    }
                ],
                "createdAt": "2018-08-09T11:15:11.083Z",
                "updatedAt": null
            }
        ]
    }
}

#######################################################################################################################
Adding Test Data for auto validation:

Query:
const addTestDataQuery = `
    mutation AddTestData($input: addTestDataInput!){
      addTestData(input: $input){
        changedTestDataEdge{
          node{
              serviceid
              utterances{
                utterance
                tags{
                  start
                  end
                  tag
                  entity
                }
                intent
              }
          }
        }
      }
    }
`;

Request URL:
http://ice-xd.southindia.cloudapp.azure.com:3001/project/configure/5c6f9dfb6e081837537ee544
5c6f9dfb6e081837537ee544 is the project id.

POST Data:
{
    "input": {
        "clientMutationId": "random",
        "utterances": [
            {
                "utterance": "frrf",
                "intent": "",
                "tags": [
                    {
                        "start": 0,
                        "tag": "TYPE",
                        "end": 1,
                        "entity": "frrf"
                    }
                ]
            }
        ],
        "serviceid": "0AdREkEwYbPydZg77pBBBs8c4ML10ZuqlPys3Cdm2lEYPBSB9M8tHCvcb9bcvF2b"
    }
}

JSON Response:
{
    "data": {
        "addTestData": {
            "changedTestDataEdge": {
                "node": {
                    "serviceid": "0AdREkEwYbPydZg77pBBBs8c4ML10ZuqlPys3Cdm2lEYPBSB9M8tHCvcb9bcvF2b",
                    "utterances": [
                        {
                            "utterance": "frrf",
                            "tags": [
                                {
                                    "start": 0,
                                    "end": 1,
                                    "tag": "TYPE",
                                    "entity": "frrf"
                                }
                            ],
                            "intent": ""
                        }
                    ]
                }
            }
        }
    }
}
#######################################################################################################################
Update Test Data for auto validation:

Query:
const updateTestDataQuery = ` mutation UpdateTestData($input: updateTestDataInput!){
    updateTestData(input: $input){
      changedTestData{
        utterances{
          utterance
          tags{
            start
            end
            tag
            entity
          }
          intent
        }
      }
    }
  }
  `;

Request URL:
http://ice-xd.southindia.cloudapp.azure.com:3001/project/configure/5c6f9dfb6e081837537ee544
5c6f9dfb6e081837537ee544 is the project id.

POST Data:
{
    "input": {
        "clientMutationId": "random",
        "id": "5d148910144b351403312ee4",
        "utterances": [
            {
                "utterance": "frrfh",
                "tags": [
                    {
                        "start": 0,
                        "tag": "CATEGORY",
                        "end": 1,
                        "entity": "frrfh"
                    }
                ],
                "intent": ""
            }
        ],
        "serviceid": "0AdREkEwYbPydZg77pBBBs8c4ML10ZuqlPys3Cdm2lEYPBSB9M8tHCvcb9bcvF2b"
    }
}

JSON Response:
{
    "data": {
        "updateTestData": {
            "changedTestData": {
                "utterances": [
                    {
                        "utterance": "frrfh",
                        "tags": [
                            {
                                "start": 0,
                                "end": 1,
                                "tag": "CATEGORY",
                                "entity": "frrfh"
                            }
                        ],
                        "intent": ""
                    }
                ]
            }
        }
    }
}

#######################################################################################################################
Load test data for auto-validation:

Query:
const loadTestDataQuery = ` query GetTestData($serviceid: String!){
    testdatas(serviceid: $serviceid){
      id
      _id
      serviceid
      utterances{
        utterance
        tags{
          start
          end
          tag
          entity
        }
        intent
      }
    }
  }
  `;
Request URL:
http://ice-xd.southindia.cloudapp.azure.com:3001/project/configure/5c6f9dfb6e081837537ee544
5c6f9dfb6e081837537ee544 is the project id.

POST Data:
{"serviceid":"0AdREkEwYbPydZg77pBBBs8c4ML10ZuqlPys3Cdm2lEYPBSB9M8tHCvcb9bcvF2b"}

JSON Response:
{
    "data": {
        "testdatas": [
            {
                "id": "VGVzdERhdGE6NWQxNDg5MTAxNDRiMzUxNDAzMzEyZWU0",
                "_id": "5d148910144b351403312ee4",
                "serviceid": "0AdREkEwYbPydZg77pBBBs8c4ML10ZuqlPys3Cdm2lEYPBSB9M8tHCvcb9bcvF2b",
                "utterances": [
                    {
                        "utterance": "frrfh",
                        "tags": [
                            {
                                "start": 0,
                                "end": 1,
                                "tag": "CATEGORY",
                                "entity": "frrfh"
                            }
                        ],
                        "intent": ""
                    }
                ]
            }
        ]
    }
}

#######################################################################################################################
Load utterances:

Query:
const getUtterancesQuery = ` query GetDatasource($dbid:ID!){
  datasource(id:$dbid){
       utterances {
         utterance
         case_converted_utterance
         mapping
         ner_trained
         ir_trained
         _id
       }
     }
}`;

Request URL:
http://ice-xd.southindia.cloudapp.azure.com:3001/project/configure/5ce522646e08183753dc4349
5ce522646e08183753dc4349 is the project id.

POST Data:
{"id":"5ce522646e08183753dc4349","dbid":"RGF0YXNvdXJjZTo1Y2U1MjI2NTZlMDgxODM3NTNkYzQzNGI="}

JSON Response:
{
    "data": {
        "datasource": {
            "utterances": [
                {
                    "utterance": "flight",
                    "case_converted_utterance": "Flight",
                    "mapping": "{\"tokens\":[\"Flight\"],\"tags\":[{\"start\":0,\"tag\":\"FLIGHT\",\"end\":1,\"score\":0.9149290001949938,\"entity\":\"flight\"}],\"intent\":\"travel\"}",
                    "ner_trained": true,
                    "ir_trained": true,
                    "_id": "5d148f36144b35140332b51d"
                },
                {
                    "utterance": "air ways is a hot air balloons",
                    "case_converted_utterance": "Air ways is a hot air balloons",
                    "mapping": "{\"tokens\":[\"Air\",\"ways\",\"is\",\"a\",\"hot\",\"air\",\"balloons\"],\"tags\":[{\"start\":0,\"tag\":\"FLIGHT\",\"end\":2,\"score\":0.9572268311681059,\"entity\":\"air ways\"},{\"start\":4,\"tag\":\"TRANSPORT\",\"end\":7,\"score\":0.9930937548156228,\"entity\":\"hot air balloons\"}],\"intent\":\"travel\"}",
                    "ner_trained": true,
                    "ir_trained": true,
                    "_id": "5d148f36144b35140332b51c"
                },
                {
                    "utterance": "air way means flight",
                    "case_converted_utterance": "Air way means flight",
                    "mapping": "{\"tokens\":[\"Air\",\"way\",\"means\",\"flight\"],\"tags\":[{\"start\":0,\"tag\":\"FLIGHT\",\"end\":2,\"entity\":\"air way\"},{\"start\":3,\"tag\":\"FLIGHT\",\"end\":4,\"entity\":\"flight\"}],\"intent\":\"testingairway\"}",
                    "ner_trained": true,
                    "ir_trained": true,
                    "_id": "5d148f36144b35140332b51b"
                },
                {
                    "utterance": "flight is going by air",
                    "case_converted_utterance": "Flight is going by air",
                    "mapping": "{\"tokens\":[\"Flight\",\"is\",\"going\",\"by\",\"air\"],\"tags\":[{\"start\":4,\"tag\":\"FLIGHT\",\"end\":5,\"score\":0.7708234676830357,\"entity\":\"air\"},{\"start\":0,\"tag\":\"FLIGHT\",\"end\":1,\"entity\":\"flight\"}],\"intent\":\"testingairway\"}",
                    "ner_trained": true,
                    "ir_trained": true,
                    "_id": "5d148f36144b35140332b51a"
                },
                {
                    "utterance": "flight is best for transport",
                    "case_converted_utterance": "Flight is best for transport",
                    "mapping": "{\"tokens\":[\"Flight\",\"is\",\"best\",\"for\",\"transport\"],\"tags\":[{\"start\":4,\"tag\":\"TRANSPORT\",\"end\":5,\"score\":0.6601473542296747,\"entity\":\"transport\"},{\"start\":0,\"tag\":\"FLIGHT\",\"end\":1,\"entity\":\"flight\"}],\"intent\":\"testingairway\"}",
                    "ner_trained": true,
                    "ir_trained": true,
                    "_id": "5d148f36144b35140332b519"
                },
                {
                    "utterance": "transport will be feasible if there is a hot air balloon",
                    "case_converted_utterance": "Transport will be feasible if there is a hot air balloon",
                    "mapping": "{\"tokens\":[\"Transport\",\"will\",\"be\",\"feasible\",\"if\",\"there\",\"is\",\"a\",\"hot\",\"air\",\"balloon\"],\"tags\":[{\"start\":0,\"tag\":\"TRANSPORT\",\"end\":1,\"score\":0.9348439254759315,\"entity\":\"transport\"},{\"start\":8,\"tag\":\"TRANSPORT\",\"end\":11,\"score\":0.9850981637400146,\"entity\":\"hot air balloon\"}],\"intent\":\"travel\"}",
                    "ner_trained": true,
                    "ir_trained": true,
                    "_id": "5d148f36144b35140332b518"
                },
                {
                    "utterance": "to move is to transport",
                    "case_converted_utterance": "To move is to transport",
                    "mapping": "{\"tokens\":[\"To\",\"move\",\"is\",\"to\",\"transport\"],\"tags\":[{\"start\":4,\"tag\":\"TRANSPORT\",\"end\":5,\"entity\":\"transport\"}],\"intent\":\"travel\"}",
                    "ner_trained": true,
                    "ir_trained": true,
                    "_id": "5d148f36144b35140332b517"
                },
                {
                    "utterance": "hot air balloon is a mode of transport",
                    "case_converted_utterance": "Hot air balloon is a mode of transport",
                    "mapping": "{\"tokens\":[\"Hot\",\"air\",\"balloon\",\"is\",\"a\",\"mode\",\"of\",\"transport\"],\"tags\":[{\"start\":0,\"tag\":\"TRANSPORT\",\"end\":3,\"score\":0.9955168700947078,\"entity\":\"hot air balloon\"},{\"start\":7,\"tag\":\"TRANSPORT\",\"end\":8,\"entity\":\"transport\"}],\"intent\":\"travel\"}",
                    "ner_trained": true,
                    "ir_trained": true,
                    "_id": "5d148f36144b35140332b516"
                },
                {
                    "utterance": "transport is an easy means to travel",
                    "case_converted_utterance": "Transport is an easy means to travel",
                    "mapping": "{\"tokens\":[\"Transport\",\"is\",\"an\",\"easy\",\"means\",\"to\",\"travel\"],\"tags\":[{\"start\":0,\"tag\":\"TRANSPORT\",\"end\":1,\"entity\":\"transport\"}],\"intent\":\"travel\"}",
                    "ner_trained": true,
                    "ir_trained": true,
                    "_id": "5d148f36144b35140332b515"
                },
                {
                    "utterance": "hot air balloon is a large balloon",
                    "case_converted_utterance": "Hot air balloon is a large balloon",
                    "mapping": "{\"tokens\":[\"Hot\",\"air\",\"balloon\",\"is\",\"a\",\"large\",\"balloon\"],\"tags\":[{\"start\":0,\"tag\":\"TRANSPORT\",\"end\":3,\"entity\":\"hot air balloon\"},{\"start\":2,\"tag\":\"TRANSPORT\",\"end\":3,\"entity\":\"balloon\"}],\"intent\":\"travel\"}",
                    "ner_trained": true,
                    "ir_trained": true,
                    "_id": "5d148f36144b35140332b514"
                },
                {
                    "utterance": "hot air balloon is not for kids",
                    "case_converted_utterance": "Hot air balloon is not for kids",
                    "mapping": "{\"tokens\":[\"Hot\",\"air\",\"balloon\",\"is\",\"not\",\"for\",\"kids\"],\"tags\":[{\"start\":0,\"tag\":\"TRANSPORT\",\"end\":3,\"entity\":\"hot air balloon\"}],\"intent\":\"travel\"}",
                    "ner_trained": true,
                    "ir_trained": true,
                    "_id": "5d148f36144b35140332b513"
                },
                {
                    "utterance": "Travelling by hot air balloon has been my dream",
                    "case_converted_utterance": "Travelling by hot air balloon has been my dream",
                    "mapping": "{\"tokens\":[\"Travelling\",\"by\",\"hot\",\"air\",\"balloon\",\"has\",\"been\",\"my\",\"dream\"],\"tags\":[{\"start\":2,\"tag\":\"TRANSPORT\",\"end\":5,\"entity\":\"hot air balloon\"}],\"intent\":\"travel\"}",
                    "ner_trained": true,
                    "ir_trained": true,
                    "_id": "5d148f36144b35140332b512"
                },
                {
                    "utterance": "air way is the best mode of transport",
                    "case_converted_utterance": "Air way is the best mode of transport",
                    "mapping": "{\"tokens\":[\"Air\",\"way\",\"is\",\"the\",\"best\",\"mode\",\"of\",\"transport\"],\"tags\":[{\"start\":0,\"tag\":\"FLIGHT\",\"end\":2,\"score\":0.6333987695101926,\"entity\":\"air way\"},{\"start\":7,\"tag\":\"TRANSPORT\",\"end\":8,\"entity\":\"transport\"}],\"intent\":\"testingairway\"}",
                    "ner_trained": true,
                    "ir_trained": true,
                    "_id": "5d148f36144b35140332b511"
                },
                {
                    "utterance": "Travelling by air is a wonderful feeling",
                    "case_converted_utterance": "Travelling by air is a wonderful feeling",
                    "mapping": "{\"tokens\":[\"Travelling\",\"by\",\"air\",\"is\",\"a\",\"wonderful\",\"feeling\"],\"tags\":[{\"start\":2,\"tag\":\"FLIGHT\",\"end\":3,\"entity\":\"air\"}],\"intent\":\"testingairway\"}",
                    "ner_trained": true,
                    "ir_trained": true,
                    "_id": "5d148f36144b35140332b510"
                },
                {
                    "utterance": "I travel by air",
                    "case_converted_utterance": "I travel by air",
                    "mapping": "{\"tokens\":[\"I\",\"travel\",\"by\",\"air\"],\"tags\":[{\"start\":3,\"tag\":\"FLIGHT\",\"end\":4,\"score\":0.6307920792417945,\"entity\":\"air\"}],\"intent\":\"testingairway\"}",
                    "ner_trained": true,
                    "ir_trained": true,
                    "_id": "5d148f36144b35140332b50f"
                }
            ]
        }
    }
}

#######################################################################################################################
Get Markdown:

Query:
const getMarkDownQuery = ` query GetProjectConfig($id: ID!){
    projectconfigs(project: $id){
      integration_markdown
    }
  }
  `;

Request URL:
http://ice-xd.southindia.cloudapp.azure.com:3001/project/configure/5bd19ab4a973d070442356e2
5bd19ab4a973d070442356e2 is the project id.

POST Data:
{"id":"5bd19ab4a973d070442356e2"}

JSON Response:
{
    "data": {
        "projectconfigs": [
            {
                "integration_markdown": "\n## Integration\nTo integrate 0AS8Q0Zd9ptR0ee4wj1qxZe4o4TtMf5wLKkeUxv3AEcvOXKWlFjzxpAySxboO9Wn with your application use the following rest endpoint\n\nhttp://ice-xd.southindia.cloudapp.azure.com:8021/api/parse/predict\n\n#### Sample Request JSON\n```json\n{\n   \"text\": \"ded\",\n   \"serviceid\":\"0AS8Q0Zd9ptR0ee4wj1qxZe4o4TtMf5wLKkeUxv3AEcvOXKWlFjzxpAySxboO9Wn\",\n   \"pos\":false,\n   \"intent\":true,\n   \"entity\":true\n}\n```\n#### Sample Response JSON\n```json\n\"text\": \"ded\",\n\n\"intent\":{\n    \"top_intent\":top intent,\n    \"confidence_level\":[\n    {\n        intent1:percentage,\n        intent2:percenatge\n    }\n    \n    ] \n}\n\n\"entities\":\n[ {\n    \"start\": start_index,\n    \"tag\": \"entity_value\",\n    \"end\": end_index,\n    \"score\": score,\n    \"entity\": \"entity_type\"\n} ]\n\n```\n"
            }
        ]
    }
}

#######################################################################################################################
