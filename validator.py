from modules.stack import Stack
from modules.tagdictionary import TAGS

def is_valid(html_string):
    tag_stack = Stack()
    
if __name__ == "__main__":
    is_valid("""<html>
                    <head>
                        <title>example</title>
                        <meta charset="utf8">
                    </head>
                    <body>
                        <h1>example</h1>
                        <ul>
                            <li>red</li>
                            <li>green</li>
                            <li>purple</li>
                        </ul>
                        <img src="redpanda.png" alt="cute red panda pic">
                        <table>
                            <thead>
                                <tr>
                                    <th>zoo location</th>
                                    <th>name</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>London</td>
                                    <td>Akiko</td>
                                </tr>
                                <tr>
                                    <td>Paris</td>
                                    <td>Kobayashi</td>
                                </tr>
                                <tr>
                                    <td>San Francisco</td>
                                    <td>Mikan</td>
                                </tr>
                                <tr>
                                    <td>Abu Dhabi</td>
                                    <td>Kyo</td>
                                </tr>
                            </tbody>
                        </table>
                    </body>
                </html>""")
    
    