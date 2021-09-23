# __pragma__('skip')
def MetaMaskOnboarding(val):
    return None

def __new__(obj):
    return obj

class window:
    addEventListener = None
    ethereum = None
    
class document:
    getElementById = None

class console:
    log = None
    error = None
# __pragma__('noskip')


forwarderOrigin = 'http://localhost:9010'


def initialize():
    # Basic Actions Section
    onboardButton = document.getElementById('connectButton')
    getAccountsButton = document.getElementById('getAccounts')
    getAccountsResult = document.getElementById('getAccountsResult')
    
    # Created check function to see if the MetaMask extension is installed
    def isMetaMaskInstalled():
        # Have to check the ethereum binding on the window object to see if it's installed
        try:
            ethereum = window.ethereum
            return ethereum and ethereum.isMetaMask
        except Exception:
            return False

    # We create a new MetaMask onboarding object to use in our app
    onboarding = __new__(MetaMaskOnboarding(forwarderOrigin))
    
    # This will start the onboarding proccess
    def onClickInstall():
        onboardButton.innerText = 'Onboarding in progress'
        onboardButton.disabled = True
        # On this object we have startOnboarding which will start the onboarding process for our end user
        onboarding.startOnboarding()

    async def onClickConnect():
        try:
            # Will open the MetaMask UI
            # You should disable this button while the request is pending!
            await window.ethereum.request({'method': 'eth_requestAccounts'})
        except Exception as error:
            console.error(error)

    def MetaMaskClientCheck():
        # Now we check to see if Metmask is installed
        if not isMetaMaskInstalled():
            # If it isn't installed we ask the user to click to install it
            onboardButton.innerText = 'Click here to install MetaMask!'
            # When the button is clicked we call th is function
            onboardButton.onclick = onClickInstall
            # The button is now disabled
            onboardButton.disabled = False
        else:
            # If MetaMask is installed we ask the user to connect to their wallet
            onboardButton.innerText = 'Connect'
            # When the button is clicked we call this function to connect the users MetaMask Wallet
            onboardButton.onclick = onClickConnect
            # The button is now disabled
            onboardButton.disabled = False

    MetaMaskClientCheck()

    async def handleGetAccountsButton():
        # we use eth_accounts because it returns a list of addresses owned by us.
        accounts = await window.ethereum.request({'method': 'eth_accounts'})
        # We take the first address in the array of addresses and display it
        getAccountsResult.innerHTML = accounts[0] or 'Not able to get accounts'

    # Eth_Accounts-getAccountsButton
    getAccountsButton.addEventListener('click', handleGetAccountsButton)


window.addEventListener('DOMContentLoaded', initialize)
