type Enum<E> = Record<keyof E, number | string> & { [k: number]: string };
/**
 * Get the array of choices for React-admin selects from an enum
 */
export function getChoicesFromEnum<E extends Enum<E>>(theEnum: E) {
  return Object.entries(theEnum)
    .filter(([key]) => isNaN(Number(key)))
    .map(([key, value]) => ({ id: value, name: key }));
}

export function downloadFileFromBuffer(buffer: Array<any>, filename: string) {
  const blob = new Blob(buffer);
  const blobURL = URL.createObjectURL(blob);
  const domElement = document.createElement("a");
  domElement.href = blobURL;
  domElement.download = filename;
  domElement.click();
  URL.revokeObjectURL(blobURL);
}

export function fileToBase64(file: File) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = () => {
      const dataURIParts = (reader.result as string).split(",");
      const base64Data = dataURIParts[dataURIParts.length - 1];
      resolve(base64Data);
    };
    reader.onerror = reject;
    reader.readAsDataURL(file);
  });
}

/**
 * https://stackoverflow.com/questions/30106476/using-javascripts-atob-to-decode-base64-doesnt-properly-decode-utf-8-strings
 */
export function b64DecodeUnicode(str) {
  return decodeURIComponent(
    atob(str)
      .split("")
      .map(function (c) {
        return "%" + ("00" + c.charCodeAt(0).toString(16)).slice(-2);
      })
      .join("")
  );
}

/**
 * Given a fetch reponse whose binary content is a PDF, opens the
 * PDF in a browser window. The URL for the open file expires after some time.
 *
 * @param {Response} response
 */
export async function openPDFFromResponse(response) {
  const pdfURL = URL.createObjectURL(await response.blob());
  window.open(pdfURL);
  setTimeout(() => URL.revokeObjectURL(pdfURL), 60000);
}
