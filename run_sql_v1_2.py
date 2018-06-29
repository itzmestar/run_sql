import argparse
import subprocess
import os

#########config section###########
DB_PATH="sqlplus"
USER=""
PASS=""
TNS=""
cmd = [DB_PATH]

def list_files(directory, ext):
    files=os.listdir(directory)
    fx=[ f for f in files if f.endswith('.' + ext)]
    return fx
    
def main(directory):
    cmd.append("{}/{}@{}".format(USER, PASS, TNS))

    filenames=list_files(directory, 'sql')
    for file in filenames:
        cmd.append("@{}".format(directory+'/'+file))
        print("\n\n=======================================================")
        print("\nRunning SQL command:")
        for i in cmd:
            print(i, end='')
            print(' ', end='')
    
        # returns output as byte string
        returned_output = subprocess.check_output(cmd)

        print('Sql output:', returned_output.decode("utf-8"))

        cmd.pop(len(cmd) - 1)
    


if __name__ == "__main__":
    """
    Execution starts here.
    """

    parser = argparse.ArgumentParser(description='Run SQL script.')
    parser.add_argument('-u', '--user', help='Oracle user', type=str, required=True)
    parser.add_argument('-p', '--pwd', help='Oracle user password', type=str, required=True)
    parser.add_argument('-t', '--tns', help='Oracle service name', type=str, required=True)
    parser.add_argument('-s', '--sql', help='SQL file directory', type=str, required=True)
    args = parser.parse_args()

    USER=args.user
    PASS=args.pwd
    TNS=args.tns

    if os.path.isdir(args.sql):
        main(args.sql)
    else:
        print('Provide a valid directory!')


    
