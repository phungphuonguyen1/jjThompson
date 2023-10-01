**Structure:**  
`views`: contains views which are rendered on navigation.  
`main`: the root, contains navigation function, some settings and activation of navigation.  
`utils`: contains some utilities & navbar component.  
`PATHS`: contains paths for navbar & settings.  

`How it works?`
There are 2 things injected into the page.
1. The component itself, the navbar with the icon & drop down.
2. The JS which is injected via `from streamlit.components.v1 import html` which allows to inject an iframe with JS.

To actually interact from withing the iframe in part 2, I am using `window.parent.document.getElementsBy...` which allows interaction from withing the dataframe with the parent document, which allows me to use JS in the places it's required.
