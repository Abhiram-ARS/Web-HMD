class API:
    def launchAPI():
        from flask import Flask, request, jsonify
        from flask_cors import CORS
        import art

        print('\n\n=================================================================================')
        print(art.text2art("Web-HMD", font="slant"),end='')
        print("      Website Hashing for Modification Detection ")
        print('=================================================================================\n\n')
        app = Flask(__name__)
        CORS(app, resources={r"/*": {"origins": "*"}})

        @app.route('/upload', methods=['POST'])
        def upload():
            try:
                from Main import Main

                funct = request.form.get('funct')
                link = request.form.get('link')
                if funct == 'ch':
                    hash_text = request.form.get('hash')
                    input = {'function':funct,'url':link,'hash':hash_text}
                    output = Main.compareHash(input)

                elif funct == 'gh':
                    input = {'function':funct,'url':link}
                    output = Main.generateHash(input)

                return jsonify(output), 200

            except Exception as e:
                return jsonify({'status':0,'error': str(e)}), 500
            
        @app.errorhandler(Exception)
        def handle_exception(e):
            return jsonify({'status':0,"error": str(e)}), 500

        if __name__ == '__main__':
            app.run(port=5000,debug=True)

API.launchAPI()