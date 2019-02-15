# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.person_beta_detaljer import PersonBetaDetaljer  
from idfy_sdk.models.person_beta_sammendrag import PersonBetaSammendrag  
from idfy_sdk.models.person_delomrader import PersonDelomrader  
from idfy_sdk.models.person_disponibel_inntekt import PersonDisponibelInntekt  
from idfy_sdk.models.person_eiendom_liste import PersonEiendomListe  
from idfy_sdk.models.person_eiendom_norge import PersonEiendomNorge  
from idfy_sdk.models.person_fullmakt_foretak import PersonFullmaktForetak  
from idfy_sdk.models.person_identifikasjon import PersonIdentifikasjon  
from idfy_sdk.models.person_ligning import PersonLigning  
from idfy_sdk.models.person_losore import PersonLosore  
from idfy_sdk.models.person_meldinger import PersonMeldinger  
from idfy_sdk.models.person_narings_interesser import PersonNaringsInteresser  
from idfy_sdk.models.person_navn_adresse import PersonNavnAdresse  
from idfy_sdk.models.person_scoring import PersonScoring  
from idfy_sdk.models.person_tidligere_navn_adresse import PersonTidligereNavnAdresse  


class PersonHentPersonResponse(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'identifikasjon_field': 'PersonIdentifikasjon',
        'navn_adresse_field': 'PersonNavnAdresse',
        'scoring_field': 'PersonScoring',
        'delomrader_field': 'list[PersonDelomrader]',
        'beta_sammendrag_field': 'PersonBetaSammendrag',
        'beta_detaljer_field': 'list[PersonBetaDetaljer]',
        'ligning_field': 'list[PersonLigning]',
        'disponibel_inntekt_field': 'list[PersonDisponibelInntekt]',
        'narings_interesser_field': 'list[PersonNaringsInteresser]',
        'eiendom_norge_field': 'PersonEiendomNorge',
        'eiendom_liste_field': 'list[PersonEiendomListe]',
        'losore_field': 'list[PersonLosore]',
        'tidligere_navn_adresse_field': 'list[PersonTidligereNavnAdresse]',
        'fullmakt_foretak_field': 'list[PersonFullmaktForetak]',
        'meldinger_field': 'list[PersonMeldinger]'
    }

    attribute_map = {
        'identifikasjon_field': 'identifikasjonField',
        'navn_adresse_field': 'navnAdresseField',
        'scoring_field': 'scoringField',
        'delomrader_field': 'delomraderField',
        'beta_sammendrag_field': 'betaSammendragField',
        'beta_detaljer_field': 'betaDetaljerField',
        'ligning_field': 'ligningField',
        'disponibel_inntekt_field': 'disponibelInntektField',
        'narings_interesser_field': 'naringsInteresserField',
        'eiendom_norge_field': 'eiendomNorgeField',
        'eiendom_liste_field': 'eiendomListeField',
        'losore_field': 'losoreField',
        'tidligere_navn_adresse_field': 'tidligereNavnAdresseField',
        'fullmakt_foretak_field': 'fullmaktForetakField',
        'meldinger_field': 'meldingerField'
    }

    def __init__(self, identifikasjon_field=None, navn_adresse_field=None, scoring_field=None, delomrader_field=None, beta_sammendrag_field=None, beta_detaljer_field=None, ligning_field=None, disponibel_inntekt_field=None, narings_interesser_field=None, eiendom_norge_field=None, eiendom_liste_field=None, losore_field=None, tidligere_navn_adresse_field=None, fullmakt_foretak_field=None, meldinger_field=None):  
        """PersonHentPersonResponse"""  

        self._identifikasjon_field = None
        self._navn_adresse_field = None
        self._scoring_field = None
        self._delomrader_field = None
        self._beta_sammendrag_field = None
        self._beta_detaljer_field = None
        self._ligning_field = None
        self._disponibel_inntekt_field = None
        self._narings_interesser_field = None
        self._eiendom_norge_field = None
        self._eiendom_liste_field = None
        self._losore_field = None
        self._tidligere_navn_adresse_field = None
        self._fullmakt_foretak_field = None
        self._meldinger_field = None
        self.discriminator = None

        if identifikasjon_field is not None:
            self.identifikasjon_field = identifikasjon_field
        if navn_adresse_field is not None:
            self.navn_adresse_field = navn_adresse_field
        if scoring_field is not None:
            self.scoring_field = scoring_field
        if delomrader_field is not None:
            self.delomrader_field = delomrader_field
        if beta_sammendrag_field is not None:
            self.beta_sammendrag_field = beta_sammendrag_field
        if beta_detaljer_field is not None:
            self.beta_detaljer_field = beta_detaljer_field
        if ligning_field is not None:
            self.ligning_field = ligning_field
        if disponibel_inntekt_field is not None:
            self.disponibel_inntekt_field = disponibel_inntekt_field
        if narings_interesser_field is not None:
            self.narings_interesser_field = narings_interesser_field
        if eiendom_norge_field is not None:
            self.eiendom_norge_field = eiendom_norge_field
        if eiendom_liste_field is not None:
            self.eiendom_liste_field = eiendom_liste_field
        if losore_field is not None:
            self.losore_field = losore_field
        if tidligere_navn_adresse_field is not None:
            self.tidligere_navn_adresse_field = tidligere_navn_adresse_field
        if fullmakt_foretak_field is not None:
            self.fullmakt_foretak_field = fullmakt_foretak_field
        if meldinger_field is not None:
            self.meldinger_field = meldinger_field

    @property
    def identifikasjon_field(self):
        """Gets the identifikasjon_field of this PersonHentPersonResponse.  


        :return: The identifikasjon_field of this PersonHentPersonResponse.  
        :rtype: PersonIdentifikasjon
        """
        return self._identifikasjon_field

    @identifikasjon_field.setter
    def identifikasjon_field(self, identifikasjon_field):
        """Sets the identifikasjon_field of this PersonHentPersonResponse.


        :param identifikasjon_field: The identifikasjon_field of this PersonHentPersonResponse.  
        :type: PersonIdentifikasjon
        """

        self._identifikasjon_field = identifikasjon_field

    @property
    def navn_adresse_field(self):
        """Gets the navn_adresse_field of this PersonHentPersonResponse.  


        :return: The navn_adresse_field of this PersonHentPersonResponse.  
        :rtype: PersonNavnAdresse
        """
        return self._navn_adresse_field

    @navn_adresse_field.setter
    def navn_adresse_field(self, navn_adresse_field):
        """Sets the navn_adresse_field of this PersonHentPersonResponse.


        :param navn_adresse_field: The navn_adresse_field of this PersonHentPersonResponse.  
        :type: PersonNavnAdresse
        """

        self._navn_adresse_field = navn_adresse_field

    @property
    def scoring_field(self):
        """Gets the scoring_field of this PersonHentPersonResponse.  


        :return: The scoring_field of this PersonHentPersonResponse.  
        :rtype: PersonScoring
        """
        return self._scoring_field

    @scoring_field.setter
    def scoring_field(self, scoring_field):
        """Sets the scoring_field of this PersonHentPersonResponse.


        :param scoring_field: The scoring_field of this PersonHentPersonResponse.  
        :type: PersonScoring
        """

        self._scoring_field = scoring_field

    @property
    def delomrader_field(self):
        """Gets the delomrader_field of this PersonHentPersonResponse.  


        :return: The delomrader_field of this PersonHentPersonResponse.  
        :rtype: list[PersonDelomrader]
        """
        return self._delomrader_field

    @delomrader_field.setter
    def delomrader_field(self, delomrader_field):
        """Sets the delomrader_field of this PersonHentPersonResponse.


        :param delomrader_field: The delomrader_field of this PersonHentPersonResponse.  
        :type: list[PersonDelomrader]
        """

        self._delomrader_field = delomrader_field

    @property
    def beta_sammendrag_field(self):
        """Gets the beta_sammendrag_field of this PersonHentPersonResponse.  


        :return: The beta_sammendrag_field of this PersonHentPersonResponse.  
        :rtype: PersonBetaSammendrag
        """
        return self._beta_sammendrag_field

    @beta_sammendrag_field.setter
    def beta_sammendrag_field(self, beta_sammendrag_field):
        """Sets the beta_sammendrag_field of this PersonHentPersonResponse.


        :param beta_sammendrag_field: The beta_sammendrag_field of this PersonHentPersonResponse.  
        :type: PersonBetaSammendrag
        """

        self._beta_sammendrag_field = beta_sammendrag_field

    @property
    def beta_detaljer_field(self):
        """Gets the beta_detaljer_field of this PersonHentPersonResponse.  


        :return: The beta_detaljer_field of this PersonHentPersonResponse.  
        :rtype: list[PersonBetaDetaljer]
        """
        return self._beta_detaljer_field

    @beta_detaljer_field.setter
    def beta_detaljer_field(self, beta_detaljer_field):
        """Sets the beta_detaljer_field of this PersonHentPersonResponse.


        :param beta_detaljer_field: The beta_detaljer_field of this PersonHentPersonResponse.  
        :type: list[PersonBetaDetaljer]
        """

        self._beta_detaljer_field = beta_detaljer_field

    @property
    def ligning_field(self):
        """Gets the ligning_field of this PersonHentPersonResponse.  


        :return: The ligning_field of this PersonHentPersonResponse.  
        :rtype: list[PersonLigning]
        """
        return self._ligning_field

    @ligning_field.setter
    def ligning_field(self, ligning_field):
        """Sets the ligning_field of this PersonHentPersonResponse.


        :param ligning_field: The ligning_field of this PersonHentPersonResponse.  
        :type: list[PersonLigning]
        """

        self._ligning_field = ligning_field

    @property
    def disponibel_inntekt_field(self):
        """Gets the disponibel_inntekt_field of this PersonHentPersonResponse.  


        :return: The disponibel_inntekt_field of this PersonHentPersonResponse.  
        :rtype: list[PersonDisponibelInntekt]
        """
        return self._disponibel_inntekt_field

    @disponibel_inntekt_field.setter
    def disponibel_inntekt_field(self, disponibel_inntekt_field):
        """Sets the disponibel_inntekt_field of this PersonHentPersonResponse.


        :param disponibel_inntekt_field: The disponibel_inntekt_field of this PersonHentPersonResponse.  
        :type: list[PersonDisponibelInntekt]
        """

        self._disponibel_inntekt_field = disponibel_inntekt_field

    @property
    def narings_interesser_field(self):
        """Gets the narings_interesser_field of this PersonHentPersonResponse.  


        :return: The narings_interesser_field of this PersonHentPersonResponse.  
        :rtype: list[PersonNaringsInteresser]
        """
        return self._narings_interesser_field

    @narings_interesser_field.setter
    def narings_interesser_field(self, narings_interesser_field):
        """Sets the narings_interesser_field of this PersonHentPersonResponse.


        :param narings_interesser_field: The narings_interesser_field of this PersonHentPersonResponse.  
        :type: list[PersonNaringsInteresser]
        """

        self._narings_interesser_field = narings_interesser_field

    @property
    def eiendom_norge_field(self):
        """Gets the eiendom_norge_field of this PersonHentPersonResponse.  


        :return: The eiendom_norge_field of this PersonHentPersonResponse.  
        :rtype: PersonEiendomNorge
        """
        return self._eiendom_norge_field

    @eiendom_norge_field.setter
    def eiendom_norge_field(self, eiendom_norge_field):
        """Sets the eiendom_norge_field of this PersonHentPersonResponse.


        :param eiendom_norge_field: The eiendom_norge_field of this PersonHentPersonResponse.  
        :type: PersonEiendomNorge
        """

        self._eiendom_norge_field = eiendom_norge_field

    @property
    def eiendom_liste_field(self):
        """Gets the eiendom_liste_field of this PersonHentPersonResponse.  


        :return: The eiendom_liste_field of this PersonHentPersonResponse.  
        :rtype: list[PersonEiendomListe]
        """
        return self._eiendom_liste_field

    @eiendom_liste_field.setter
    def eiendom_liste_field(self, eiendom_liste_field):
        """Sets the eiendom_liste_field of this PersonHentPersonResponse.


        :param eiendom_liste_field: The eiendom_liste_field of this PersonHentPersonResponse.  
        :type: list[PersonEiendomListe]
        """

        self._eiendom_liste_field = eiendom_liste_field

    @property
    def losore_field(self):
        """Gets the losore_field of this PersonHentPersonResponse.  


        :return: The losore_field of this PersonHentPersonResponse.  
        :rtype: list[PersonLosore]
        """
        return self._losore_field

    @losore_field.setter
    def losore_field(self, losore_field):
        """Sets the losore_field of this PersonHentPersonResponse.


        :param losore_field: The losore_field of this PersonHentPersonResponse.  
        :type: list[PersonLosore]
        """

        self._losore_field = losore_field

    @property
    def tidligere_navn_adresse_field(self):
        """Gets the tidligere_navn_adresse_field of this PersonHentPersonResponse.  


        :return: The tidligere_navn_adresse_field of this PersonHentPersonResponse.  
        :rtype: list[PersonTidligereNavnAdresse]
        """
        return self._tidligere_navn_adresse_field

    @tidligere_navn_adresse_field.setter
    def tidligere_navn_adresse_field(self, tidligere_navn_adresse_field):
        """Sets the tidligere_navn_adresse_field of this PersonHentPersonResponse.


        :param tidligere_navn_adresse_field: The tidligere_navn_adresse_field of this PersonHentPersonResponse.  
        :type: list[PersonTidligereNavnAdresse]
        """

        self._tidligere_navn_adresse_field = tidligere_navn_adresse_field

    @property
    def fullmakt_foretak_field(self):
        """Gets the fullmakt_foretak_field of this PersonHentPersonResponse.  


        :return: The fullmakt_foretak_field of this PersonHentPersonResponse.  
        :rtype: list[PersonFullmaktForetak]
        """
        return self._fullmakt_foretak_field

    @fullmakt_foretak_field.setter
    def fullmakt_foretak_field(self, fullmakt_foretak_field):
        """Sets the fullmakt_foretak_field of this PersonHentPersonResponse.


        :param fullmakt_foretak_field: The fullmakt_foretak_field of this PersonHentPersonResponse.  
        :type: list[PersonFullmaktForetak]
        """

        self._fullmakt_foretak_field = fullmakt_foretak_field

    @property
    def meldinger_field(self):
        """Gets the meldinger_field of this PersonHentPersonResponse.  


        :return: The meldinger_field of this PersonHentPersonResponse.  
        :rtype: list[PersonMeldinger]
        """
        return self._meldinger_field

    @meldinger_field.setter
    def meldinger_field(self, meldinger_field):
        """Sets the meldinger_field of this PersonHentPersonResponse.


        :param meldinger_field: The meldinger_field of this PersonHentPersonResponse.  
        :type: list[PersonMeldinger]
        """

        self._meldinger_field = meldinger_field

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PersonHentPersonResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
