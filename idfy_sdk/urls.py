#The urllib module has a function called urljoin which might be able to improve how I put together these urls.

DefaultBaseUrl = "https://api.idfy.io"
DefaultOAuthBaseUrl = DefaultBaseUrl    #Could this lead to problems where the DefaultOAuthBaseUrl resets unexpectedly?
TestBaseUrl = "http://localhost:5000" #testing only

OAuthTokens = "/oauth/connect/token" #Uses OAuthBaseUrl as prefix
Signature = "/signature"
SignatureDocuments = Signature + "/documents"

Notification = "/notification"

Identification = "/identification"
IdentificationSession = Identification + "/session"
IdentificationSessionStatus = IdentificationSession + "/status"
InvalidateSession = IdentificationSession + "/invalidate"
CreateBankIdMobileSession = Identification + "/no/bankid/mobile"

Log = Identification + "/log"
RetrieveLogEntry = Log + "/requestId"
ListLogEntries = Log + "/filter"

Merchant = "/merchant"
MerchantSignature = Merchant + "/signature"

Jwt = "/jwt"

Validation = "/validation"
ValidationBankid = Validation + "/no/bankid"

Admin = "/admin"
Account = Admin + "/account"
Dealer = Admin + "/dealer"
Oauth = Admin + "/oauthclient"
Openid = Admin + "/openid"
Template = Admin + "/template"
TemplateDefaults = Template + "/defaults"
Preview = Template + "/preview"
