import datetime
import inspect
def print_log(str):
    formatted_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    current_frame = inspect.currentframe()
    caller_frame = current_frame.f_back
    file_name = caller_frame.f_code.co_filename
    line_number = caller_frame.f_lineno  
    print(f'{str}, {file_name}, {line_number}, {formatted_now}.')


def record_test_result(file_name, epoch, Recall, NDCG):
    with open(file_name, 'a') as file_test_result:
        print(f'{epoch}th epoch test result:', file=file_test_result)
        print(f'Recall: {Recall}, NDCG: {NDCG}', file=file_test_result)