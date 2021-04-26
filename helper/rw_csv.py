import csv


# read csv file as dictionary
def read_csv(testcase_name, key):
    csv_file_path = 'data/First step.csv'
    try:
        with open(csv_file_path, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if testcase_name == row["Test Id"]:
                    data = row if key == "row" else row[key]
                    return data
        test_id = ""
        assert test_id != "", f"Testcase Id not found in CSV file {csv_file_path}"

    except AssertionError as ae:
        print(f'{type(ae)}')
        err = {"error": True, "error_msg": ae}
    except Exception as e:
        err = {"error": True, "error_msg": e}
        # log.exception(str(e))
    return err


if __name__ == '__main__':
    print(read_csv("po_01"))